@echo off
setlocal

REM Define an array of required files
set "required_files= init.py installer src\ADB.py src\commands.py src\GUI.py"

REM Function to check for required files
:check_files
for %%f in (%required_files%) do (
    if not exist "%%f" (
        echo Error: Required file not found: %%f
        exit /b 1
    )
)

call :check_files

echo  █████╗ ██████╗ ██████╗    ████████╗ ██████╗  ██████╗ ██╗      ██╗███╗   ██╗███████╗████████╗ █████╗ ██╗     ██║     ███████╗██████╗ 
echo ██╔══██╗██╔══██╗██╔══██╗   ╚══██╔══╝██╔═══██╗██╔═══██╗██║      ██║████╗  ██║██╔════╝╚══██╔══╝██╔══██╗██║     ██║     ██╔════╝██╔══██╗
echo ███████║██║  ██║██████╔╝█████╗██║   ██║   ██║██║   ██║██║█████╗██║██╔██╗ ██║███████╗   ██║   ███████║██║     ██║     █████╗  ██████╔╝
echo ██╔══██║██║  ██║██╔══██╗╚════╝██║   ██║   ██║██║   ██║██║╚════╝██║██║╚██╗██║╚════██║   ██║   ██╔══██║██║     ██║     ██╔══╝  ██╔══██╗
echo ██║  ██║██████╔╝██████╔╝      ██║   ╚██████╔╝╚██████╔╝███████╗ ██║██║ ╚████║███████║   ██║   ██║  ██║███████╗███████╗███████╗██║  ██║
echo ╚═╝  ╚═╝╚═════╝ ╚═════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ ╚═╝╚═╝  ╚═══╝╚══════╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
echo                                                                                                                                     

echo Checking for Python...
python --version >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed or not in PATH. Please install Python and try again.
    pause
    exit /b 1
)

echo Creating virtual environment...
python -m venv .venv
if not exist "%CD%\.venv" (
    echo Failed to create virtual environment.
    pause
    exit /b 1
)

echo Installing requirements...
if not exist "%CD%\.venv\Scripts\pip.exe" (
    echo pip.exe not found in virtual environment.
    pause
    exit /b 1
)
"%CD%\.venv\Scripts\pip.exe" install -r requirements.txt

echo Installation complete.
pause