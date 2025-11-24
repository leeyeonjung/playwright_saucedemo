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

        stage('Collect Latest Report') {
            steps {
                sh '''
                    /bin/bash -c "
                        echo [5] 최신 HTML 리포트 찾기
                        cd $RESULT_DIR

                        LATEST_HTML=$(ls -t *.html | head -n 1)
                        echo 가장 최근 리포트: $LATEST_HTML

                        cp $RESULT_DIR/$LATEST_HTML $WORKSPACE/
                    "
                '''
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
