@echo off
setlocal
echo Creating Termyx shortcut...
powershell.exe -NoProfile -ExecutionPolicy Bypass -File "%~dp0setup.ps1" "%~dp0"
if errorlevel 1 (
    echo.
    echo Shortcut creation failed.
    pause
    exit /b 1
)
echo.
echo Done! A Termyx shortcut has been created on your desktop.
echo You can pin it to your taskbar by right-clicking it and selecting "Pin to taskbar".
echo.
pause
