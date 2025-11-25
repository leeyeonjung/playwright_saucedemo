echo [Windows] Collecting latest HTML report

cd C:\Automation\saucedemo\tests\Results

for /f "delims=" %%i in ('dir /b /od *.html') do set LATEST_HTML=%%i

if "%LATEST_HTML%"=="" (
    echo No HTML report found.
    exit /b 0
)

echo Latest report (Windows): %LATEST_HTML%
copy "C:\Automation\saucedemo\tests\Results\%LATEST_HTML%" "%WORKSPACE%\Windows_%LATEST_HTML%"

echo Windows report copied.