pipeline {
    agent { label 'web_linux' }

    environment {
        PROJECT_ROOT = "/home/ubuntu/saucedemo"
        TEST_DIR = "/home/ubuntu/saucedemo/playwright_saucedemo"
        RESULT_DIR = "/home/ubuntu/saucedemo/playwright_saucedemo/tests/Results"
        VENV = "/home/ubuntu/saucedemo/saucedemo_pytest/bin/activate"
    }

    triggers {
        githubPush()
    }

    stages {

        /* -------------------------
           1) 변경 없으면 Skip → ABORTED
        -------------------------- */
        stage('Skip Info') {
            when {
                not { changeset pattern: "playwright_saucedemo/**", comparator: "ANT" }
            }
            steps {
                echo "🟡 No changes → Skipping test execution."
                script {
                    currentBuild.result = 'ABORTED'
                    error("Stop remaining stages due to no changes.")
                }
            }
        }

        /* -------------------------
           2) 환경 준비
        -------------------------- */
        stage('Prepare Environment') {
            steps {
                sh '''
                    /bin/bash -c "
                        echo [1] 프로젝트 폴더 이동
                        cd $PROJECT_ROOT

                        echo [2] 가상환경 활성화
                        source $VENV

                        echo [3] Playwright 브라우저 설치
                        playwright install chromium
                    "
                '''
            }
        }

        /* -------------------------
           3) 테스트 실행
        -------------------------- */
        stage('Run Tests') {
            steps {
                sh '''
                    /bin/bash -c "
                        echo [4] 테스트 실행
                        cd $TEST_DIR
                        source $VENV
                        pytest -v || true
                    "
                '''
            }
        }

        /* -------------------------
           4) 최신 HTML report 복사
        -------------------------- */
        stage('Collect Latest Report') {
            steps {
                script {
                    if (currentBuild.result == 'ABORTED') {
                        echo "⏩ Build aborted → Skipping report collection."
                        return
                    }
                }

                sh '''
                    /bin/bash -c '
                        echo "[5] 최신 HTML 리포트 찾기"
                        cd "$RESULT_DIR"

                        LATEST_HTML=$(ls -t *.html 2>/dev/null | head -n 1)

                        if [ -z "$LATEST_HTML" ]; then
                            echo "❌ HTML 리포트 없음"
                            exit 0
                        fi

                        echo "가장 최근 리포트: $LATEST_HTML"

                        cp "$RESULT_DIR/$LATEST_HTML" "$WORKSPACE/$LATEST_HTML"
                        echo "✅ 복사 완료"
                    '
                '''
            }
        }
    }

    /* -------------------------
       5) post 블록: ABORTED 시 스킵
    -------------------------- */
    post {
        always {
            script {
                if (currentBuild.result == 'ABORTED') {
                    echo "⏩ Post block skipped (build was aborted)."
                    return
                }
            }

            echo "[6] HTML Report Archive"
            archiveArtifacts artifacts: '*.html', fingerprint: true, onlyIfSuccessful: false
        }
    }
}
