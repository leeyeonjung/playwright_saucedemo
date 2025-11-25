#!/bin/bash

RESULT_DIR="/home/ubuntu/saucedemo/playwright_saucedemo/tests/Results"
WORKSPACE="$WORKSPACE"

echo "[Linux] Collecting latest HTML report"

cd "$RESULT_DIR"

LATEST_HTML=$(ls -t *.html 2>/dev/null | head -n 1)

if [ -z "$LATEST_HTML" ]; then
    echo "No Linux HTML report found."
    exit 0
fi

echo "Latest report (Linux): $LATEST_HTML"
cp "$RESULT_DIR/$LATEST_HTML" "$WORKSPACE/Linux_$LATEST_HTML"

echo "Linux report copied."
