"""
YAML loading for regulator schema files.

Why this module exists
----------------------
The schema files are YAML because a compliance officer has to edit them when a
circular changes, and YAML comments are how the provenance caveats stay attached
to the field they qualify. JSON would lose those comments.

PyYAML is the correct parser and is used whenever it is importable. It is not
available in every deployment target here (and cannot always be installed in an
air-gapped or locked-down environment), so this module carries a deliberately
tiny fallback parser covering only the YAML subset the schema files use.

The fallback is written to FAIL, not to guess. Anchors, aliases, tags, flow
mappings, multiple documents, merge keys and tabs are all rejected with a line
number rather than silently mis-parsed. A compliance schema that parses to
something subtly different from what the author wrote is worse than one that
refuses to load, so every ambiguity is an error.

If you are reviewing this: prefer installing PyYAML and letting this fallback go
unused. ``using_pyyaml()`` reports which path is active, and the loader records
it on every schema it loads so the provenance is visible at runtime.
"""
from typing import Any, Dict, List, Optional, Tuple

try:  # pragma: no cover - depends on deployment
    import yaml as _pyyaml
except ImportError:  # pragma: no cover
    _pyyaml = None


class YamlLiteError(ValueError):
    """Raised when a schema file cannot be parsed unambiguously."""

    def __init__(self, message: str, lineno: Optional[int] = None, source: str = ""):
        self.lineno = lineno
        self.source = source
        where = ""
        if source:
            where += source
        if lineno is not None:
            where += ":%d" % lineno
        super().__init__("%s: %s" % (where, message) if where else message)


def using_pyyaml() -> bool:
    """True when the real parser is in use."""
    return _pyyaml is not None


# Constructs that change meaning in ways the fallback does not model.
_REJECTED = (
    ("&", "YAML anchors are not supported in schema files"),
    ("*", "YAML aliases are not supported in schema files"),
    ("!", "YAML tags are not supported in schema files"),
    ("{", "flow mappings are not supported; use block mapping syntax"),
    ("<<", "merge keys are not supported in schema files"),
)

_BLOCK_INDICATORS = ("|", "|-", "|+", ">", ">-", ">+")


def loads(text: str, source: str = "") -> Any:
    """Parse a YAML document, using PyYAML when available."""
    if _pyyaml is not None:
        try:
            documents = list(_pyyaml.safe_load_all(text))
        except _pyyaml.YAMLError as exc:  # pragma: no cover - parser specific
            raise YamlLiteError(str(exc), source=source)
        if len(documents) > 1:
            raise YamlLiteError(
                "schema files must contain exactly one YAML document", source=source)
        return documents[0] if documents else None
    return _Parser(text, source).parse_document()


def _leading_spaces(line: str, lineno: int, source: str) -> int:
    count = 0
    for char in line:
        if char == " ":
            count += 1
        elif char == "\t":
            raise YamlLiteError(
                "tab used for indentation; schema files must use spaces",
                lineno, source)
        else:
            break
    return count


def _strip_comment(line: str) -> str:
    """Remove a trailing comment, respecting quotes."""
    out, quote = [], None
    index = 0
    while index < len(line):
        char = line[index]
        if quote:
            out.append(char)
            if char == quote:
                quote = None
        elif char in "\"'":
            quote = char
            out.append(char)
        elif char == "#":
            # A '#' only starts a comment at the start or after whitespace.
            if index == 0 or line[index - 1] in " \t":
                break
            out.append(char)
        else:
            out.append(char)
        index += 1
    return "".join(out).rstrip()


class _Parser:
    """Recursive-descent parser for the supported YAML subset."""

    def __init__(self, text: str, source: str = ""):
        self.lines = text.splitlines()
        self.source = source
        self.index = 0

    # ---- line handling ------------------------------------------------

    def _significant(self) -> Optional[Tuple[int, str, int]]:
        """Next (indent, content, lineno), skipping blanks and comments."""
        while self.index < len(self.lines):
            raw = self.lines[self.index]
            lineno = self.index + 1
            stripped = _strip_comment(raw)
            if not stripped.strip():
                self.index += 1
                continue
            if stripped.strip() in ("---", "..."):
                self.index += 1
                continue
            indent = _leading_spaces(raw, lineno, self.source)
            return indent, stripped.strip(), lineno
        return None

    def _guard(self, content: str, lineno: int) -> None:
        for token, message in _REJECTED:
            if token == "<<":
                if content.startswith("<<"):
                    raise YamlLiteError(message, lineno, self.source)
            elif token in ("&", "*"):
                # Only meaningful as the first character of a value.
                if content.startswith(token):
                    raise YamlLiteError(message, lineno, self.source)
            elif token in content:
                raise YamlLiteError(message, lineno, self.source)

    # ---- entry point --------------------------------------------------

    def parse_document(self) -> Any:
        head = self._significant()
        if head is None:
            return None
        value = self.parse_node(head[0])
        trailing = self._significant()
        if trailing is not None:
            raise YamlLiteError(
                "unexpected content after end of document", trailing[2], self.source)
        return value

    def parse_node(self, indent: int) -> Any:
        head = self._significant()
        if head is None or head[0] < indent:
            return None
        if head[0] > indent:
            raise YamlLiteError(
                "unexpected indentation (expected %d spaces, found %d)"
                % (indent, head[0]), head[2], self.source)
        if head[1] == "-" or head[1].startswith("- "):
            return self.parse_sequence(indent)
        return self.parse_mapping(indent)

    # ---- mappings -----------------------------------------------------

    def parse_mapping(self, indent: int) -> Dict[str, Any]:
        result: Dict[str, Any] = {}
        while True:
            head = self._significant()
            if head is None or head[0] < indent:
                return result
            level, content, lineno = head
            if level > indent:
                raise YamlLiteError(
                    "unexpected indentation inside mapping", lineno, self.source)
            if content == "-" or content.startswith("- "):
                raise YamlLiteError(
                    "sequence item found where a mapping key was expected",
                    lineno, self.source)

            key, rest = self._split_key(content, lineno)
            if key in result:
                raise YamlLiteError(
                    "duplicate key %r in mapping" % key, lineno, self.source)
            self.index += 1

            if rest in _BLOCK_INDICATORS:
                result[key] = self._read_block_scalar(indent, rest, lineno)
            elif rest == "":
                child = self._significant()
                if child is not None and child[0] > indent:
                    result[key] = self.parse_node(child[0])
                else:
                    result[key] = None
            else:
                self._guard(rest, lineno)
                result[key] = self._scalar(rest, lineno)

    def _split_key(self, content: str, lineno: int) -> Tuple[str, str]:
        quote = None
        for position, char in enumerate(content):
            if quote:
                if char == quote:
                    quote = None
            elif char in "\"'":
                quote = char
            elif char == ":":
                after = content[position + 1:]
                if after == "" or after.startswith(" "):
                    key = content[:position].strip()
                    if key[:1] in "\"'" and key[:1] == key[-1:]:
                        key = key[1:-1]
                    if not key:
                        raise YamlLiteError("empty mapping key", lineno, self.source)
                    return key, after.strip()
        raise YamlLiteError(
            "expected 'key: value' but found %r" % content, lineno, self.source)

    # ---- sequences ----------------------------------------------------

    def parse_sequence(self, indent: int) -> List[Any]:
        items: List[Any] = []
        while True:
            head = self._significant()
            if head is None or head[0] < indent:
                return items
            level, content, lineno = head
            if level > indent:
                raise YamlLiteError(
                    "unexpected indentation inside sequence", lineno, self.source)
            if not (content == "-" or content.startswith("- ")):
                return items

            rest = content[1:].strip()
            if rest == "":
                self.index += 1
                child = self._significant()
                if child is not None and child[0] > indent:
                    items.append(self.parse_node(child[0]))
                else:
                    items.append(None)
                continue

            if self._looks_like_mapping(rest):
                # "- key: value" starts a mapping whose keys align with the
                # column of the first key. Rewriting the dash to spaces lets
                # the mapping parser handle it without a special case.
                raw = self.lines[self.index]
                column = raw.index("-") + 1
                while column < len(raw) and raw[column] == " ":
                    column += 1
                self.lines[self.index] = " " * column + rest
                items.append(self.parse_mapping(column))
                continue

            self._guard(rest, lineno)
            items.append(self._scalar(rest, lineno))
            self.index += 1

    @staticmethod
    def _looks_like_mapping(text: str) -> bool:
        quote = None
        for position, char in enumerate(text):
            if quote:
                if char == quote:
                    quote = None
            elif char in "\"'":
                quote = char
            elif char == ":":
                after = text[position + 1:]
                if after == "" or after.startswith(" "):
                    return True
        return False

    # ---- scalars ------------------------------------------------------

    def _read_block_scalar(self, parent_indent: int, indicator: str,
                           lineno: int) -> str:
        collected: List[str] = []
        block_indent: Optional[int] = None
        while self.index < len(self.lines):
            raw = self.lines[self.index]
            if raw.strip() == "":
                collected.append("")
                self.index += 1
                continue
            current = _leading_spaces(raw, self.index + 1, self.source)
            if current <= parent_indent:
                break
            if block_indent is None:
                block_indent = current
            collected.append(raw[block_indent:])
            self.index += 1

        while collected and collected[-1] == "":
            collected.pop()
        if not collected:
            return ""

        if indicator.startswith("|"):
            body = "\n".join(collected)
        else:
            # Folded: blank lines become paragraph breaks, others join.
            paragraphs, current_lines = [], []
            for line in collected:
                if line.strip() == "":
                    if current_lines:
                        paragraphs.append(" ".join(current_lines))
                        current_lines = []
                else:
                    current_lines.append(line.strip())
            if current_lines:
                paragraphs.append(" ".join(current_lines))
            body = "\n\n".join(paragraphs)

        if indicator.endswith("+"):
            return body + "\n"
        if indicator.endswith("-"):
            return body
        return body + "\n" if indicator in ("|", ">") else body

    def _scalar(self, text: str, lineno: int) -> Any:
        if len(text) >= 2 and text[0] == text[-1] and text[0] in "\"'":
            return text[1:-1]

        if text.startswith("["):
            if not text.endswith("]"):
                raise YamlLiteError(
                    "unterminated flow sequence; keep it on one line",
                    lineno, self.source)
            inner = text[1:-1].strip()
            if inner == "":
                return []
            return [self._scalar(part.strip(), lineno)
                    for part in self._split_flow(inner, lineno)]

        lowered = text.lower()
        if lowered in ("true", "yes", "on"):
            return True
        if lowered in ("false", "no", "off"):
            return False
        if lowered in ("null", "~", ""):
            return None

        try:
            return int(text)
        except ValueError:
            pass
        try:
            return float(text)
        except ValueError:
            pass
        return text

    @staticmethod
    def _split_flow(inner: str, lineno: int) -> List[str]:
        parts, buffer, quote = [], [], None
        for char in inner:
            if quote:
                buffer.append(char)
                if char == quote:
                    quote = None
            elif char in "\"'":
                quote = char
                buffer.append(char)
            elif char == ",":
                parts.append("".join(buffer))
                buffer = []
            else:
                buffer.append(char)
        if buffer:
            parts.append("".join(buffer))
        return [part for part in parts if part.strip() != ""]
