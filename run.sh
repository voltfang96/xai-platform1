#!/bin/bash
echo ""
echo "============================================================"
echo "  🔍 XAI Platform - Explainable AI for Regulated Industries"
echo "  📋 Compliant with RBI | IRDAI | SEBI | IndiaAI"
echo "  🌐 Supporting 22 Indian Languages"
echo "============================================================"
echo ""
echo "Starting server... Open http://localhost:${1:-8000} in your browser"
echo "Press Ctrl+C to stop"
echo ""
cd "$(dirname "$0")/backend"
python3 server.py ${1:-8000}
