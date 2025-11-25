#!/bin/bash

PREFIX="$1"

# --- SETUP ---
echo "[Linux] Git pull"
cd /home/ubuntu/saucedemo || exit
git fetch --all
git reset --hard origin/main

echo "[Linux] Activate venv"
source /home/ubuntu/saucedemo/saucedemo_pytest/bin/activate

echo "[Linux] Install Playwright browser"
playwright install chromium

# --- TEST ---
echo "[Linux] Run pytest"
cd /home/ubuntu/saucedemo/playwright_saucedemo || exit
pytest -v || true

# --- REPORT ---
RESULT_DIR="/home/ubuntu/saucedemo/playwright_saucedemo/tests/Results"
cd "$RESULT_DIR" || exit

LATEST=$(ls -t *.html 2>/dev/null | head -n 1)

if [ -z "$LATEST" ]; then
    echo "No Linux report found."
    exit 0
fi

NEWFILE="${PREFIX}${LATEST}"
cp "$LATEST" "$WORKSPACE/$NEWFILE"
echo "[Linux] Saved as $NEWFILE"
