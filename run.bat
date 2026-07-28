@echo off
echo ============================================================
echo   XAI Platform - Explainable AI for Regulated Industries
echo ============================================================
set PORT=%1
if "%PORT%"=="" set PORT=8000
echo Starting server on http://localhost:%PORT%
cd /d "%~dp0backend"
python server.py %PORT%
