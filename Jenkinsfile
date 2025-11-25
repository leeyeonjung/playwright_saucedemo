pipeline {
    agent none

    environment {
        // Linux 설정
        LINUX_PROJECT_ROOT = "/home/ubuntu/saucedemo"
        LINUX_TEST_DIR     = "/home/ubuntu/saucedemo/playwright_saucedemo"
        LINUX_RESULT_DIR   = "/home/ubuntu/saucedemo/playwright_saucedemo/tests/Results"
        LINUX_VENV         = "/home/ubuntu/saucedemo/saucedemo_pytest/bin/activate"

        // Windows 설정
        WIN_PROJECT_ROOT = "C:\\Automation\\saucedemo"
        WIN_RESULT_DIR   = "C:\\Automation\\saucedemo\\tests\\Results"
    }

    triggers {
        githubPush()
    }

    stages {

        stage('Skip Info') {
            when {
                not { changeset pattern: "playwright_saucedemo/**", comparator: "ANT" }
            }
            steps {
                echo "🟡 No changes → Skipping all test executions."
                script {
                    currentBuild.result = 'ABORTED'
                    echo "Stop remaining stages due to no changes."
                }
            }
        }

        stage('Parallel Playwright Tests') {
            parallel {

                stage('Linux Playwright') {
                    agent { label 'web_linux' }
                    stages {

                        stage('Linux Prepare Environment') {
                            steps {
                                sh '''
                                    /bin/bash -c "
                                        echo [Linux] 프로젝트 이동
                                        cd $LINUX_PROJECT_ROOT

                                        echo [Linux] 가상환경 활성화
                                        source $LINUX_VENV

                                        echo [Linux] Playwright 브라우저 설치
                                        playwright install chromium
                                    "
                                '''
                            }
                        }

                        stage('Linux Run Tests') {
                            steps {
                                sh '''
                                    /bin/bash -c "
                                        echo [Linux] Pytest 실행
                                        cd $LINUX_TEST_DIR
                                        source $LINUX_VENV
                                        pytest -v || true
                                    "
                                '''
                            }
                        }

                        stage('Linux Collect Report') {
                            steps {
                                sh '''
                                    /bin/bash -c '
                                        echo "[Linux] 최신 HTML 리포트 찾기"
                                        cd "$LINUX_RESULT_DIR"

                                        LATEST_HTML=$(ls -t *.html 2>/dev/null | head -n 1)

                                        if [ -z "$LATEST_HTML" ]; then
                                            echo "❌ Linux HTML 리포트 없음"
                                            exit 0
                                        fi

                                        echo "가장 최근 리포트(Linux): $LATEST_HTML"
                                        cp "$LINUX_RESULT_DIR/$LATEST_HTML" "$WORKSPACE/Linux_$LATEST_HTML"
                                        echo "✅ Linux 리포트 복사 완료"
                                    '
                                '''
                            }
                        }
                    }
                }

                stage('Windows Playwright') {
                    agent { label 'web_windows' }
                    stages {

                        stage('Windows Prepare Environment') {
                            steps {
                                bat '''
                                    echo [Windows] 프로젝트 이동
                                    cd %WIN_PROJECT_ROOT%

                                    echo [Windows] Playwright 브라우저 설치
                                    playwright install chromium
                                '''
                            }
                        }

                        stage('Windows Run Tests') {
                            steps {
                                bat '''
                                    echo [Windows] Pytest 실행
                                    cd %WIN_PROJECT_ROOT%
                                    pytest -v
                                '''
                            }
                        }

                        stage('Windows Collect Report') {
                            steps {
                                bat '''
                                    echo [Windows] 최신 HTML 리포트 찾기
                                    cd %WIN_RESULT_DIR%

                                    for /f "delims=" %%i in ('dir /b /od *.html') do set LATEST_HTML=%%i

                                    if "%LATEST_HTML%"=="" (
                                        echo ❌ Windows HTML 리포트 없음
                                        exit /b 0
                                    )

                                    echo 가장 최근 리포트(Windows): %LATEST_HTML%
                                    copy "%WIN_RESULT_DIR%\\%LATEST_HTML%" "%WORKSPACE%\\Windows_%LATEST_HTML%"
                                    echo ✔ Windows 리포트 복사 완료
                                '''
                            }
                        }

                    }
                }

            }
        }
    }

    post {
        always {
            node('web_linux') {
                script {
                    if (currentBuild.result == 'ABORTED') {
                        echo "⏩ Post block skipped (build was aborted)."
                        return
                    }
                }

                echo "[POST] HTML Report Archive"
                archiveArtifacts artifacts: '*.html', fingerprint: true, onlyIfSuccessful: false
            }
        }
    }
}
