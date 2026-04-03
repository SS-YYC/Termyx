@echo off
setlocal
cd /d "%~dp0Termyx"
where py >nul 2>nul
if not errorlevel 1 (
    py main.py
) else (
    python main.py
)
pause
