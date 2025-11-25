echo [Windows] Moving to project root
cd C:\Automation\saucedemo

echo [Windows] Fetching latest Git remote
git fetch --all

echo [Windows] Resetting to origin/main
git reset --hard origin/main

echo [Windows] Installing Playwright browser
playwright install chromium
