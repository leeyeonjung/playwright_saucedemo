@echo off
set PREFIX=%1

REM --- SETUP ---
echo [Windows] Git pull
cd C:\Automation\saucedemo
git fetch --all
git reset --hard origin/main

echo [Windows] Install Playwright
playwright install chromium

REM --- TEST ---
echo [Windows] Run pytest
cd C:\Automation\saucedemo
pytest -v

REM --- REPORT ---
cd C:\Automation\saucedemo\tests\Results

for /f "delims=" %%i in ('dir /b /od *.html') do set LATEST=%%i

if "%LATEST%"=="" (
    echo No Windows report found.
    exit /b 0
)

set NEWFILE=%PREFIX%%LATEST%
copy "%LATEST%" "%WORKSPACE%\%NEWFILE%"

echo [Windows] Saved as %NEWFILE%
