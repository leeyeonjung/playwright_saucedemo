#!/bin/bash

echo "[Linux] Running pytest"
cd /home/ubuntu/saucedemo/playwright_saucedemo
source /home/ubuntu/saucedemo/saucedemo_pytest/bin/activate
pytest -v || true
