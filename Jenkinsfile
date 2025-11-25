pipeline {
    agent none

    stages {

        stage("Parallel Playwright Tests") {
            parallel {

                stage("Linux Playwright") {
                    agent { label 'web_linux' }
                    steps {
                        sh '''
                            echo "[Linux] Playwright Install"
                            cd /home/ubuntu/saucedemo/playwright_saucedemo
                            source ../saucedemo_pytest/bin/activate
                            playwright install chromium
                            pytest -v
                        '''
                    }
                }

                stage("Windows Playwright") {
                    agent { label 'web_windows' }
                    steps {
                        bat '''
                            echo [Windows] Playwright Install
                            cd C:\\Automation\\saucedemo
                            playwright install chromium
                            pytest -v
                        '''
                    }
                }

            }
        }
    }
}
