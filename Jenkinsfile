pipeline {
    agent { label 'web_linux' }

    environment {
        PROJECT_ROOT = "/home/ubuntu/saucedemo"
        TEST_DIR = "/home/ubuntu/saucedemo/playwright_saucedemo"
        RESULT_DIR = "/home/ubuntu/saucedemo/playwright_saucedemo/tests/Results"
        VENV = "/home/ubuntu/saucedemo/saucedemo_pytest/bin/activate"
    }

    stages {

        stage('Prepare Environment') {
            steps {
                sh(script: '''
                    echo "[1] 프로젝트 폴더 이동"
                    cd "$PROJECT_ROOT"

                    echo "[2] 가상환경 활성화"
                    source "$VENV"

                ''', shell: '/bin/bash')
            }
        }

        stage('Run Tests') {
            steps {
                sh(script: '''
                    echo "[4] 테스트 실행"
                    cd "$TEST_DIR"

                    echo "[4-1] 가상환경 활성화"
                    source "$VENV"

                    echo "[4-2] pytest 실행"
                    pytest -v || true
                ''', shell: '/bin/bash')
            }
        }

        stage('Collect Latest Report') {
            steps {
                sh(script: '''
                    echo "[5] 가장 최근 HTML 리포트 찾기"

                    cd "$RESULT_DIR"

                    # 최신 파일 하나 찾기
                    LATEST_HTML=$(ls -t *.html | head -n 1)

                    echo "가장 최근 리포트: $LATEST_HTML"

                    # Jenkins workspace에 복사
                    cp "$RESULT_DIR/$LATEST_HTML" "$WORKSPACE/"
                ''', shell: '/bin/bash')
            }
        }
    }

    post {
        always {
            echo "[6] HTML Report Archive"
            archiveArtifacts artifacts: '*.html', fingerprint: true
        }
    }
}
