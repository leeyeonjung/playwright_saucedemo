#!/bin/bash

echo "[Linux] Moving to project root"
cd /home/ubuntu/saucedemo

echo "[Linux] Fetching latest Git remote"
git fetch --all

echo "[Linux] Resetting to origin/main"
git reset --hard origin/main

echo "[Linux] Activating venv"
source /home/ubuntu/saucedemo/saucedemo_pytest/bin/activate

echo "[Linux] Installing Playwright browser"
playwright install chromium
