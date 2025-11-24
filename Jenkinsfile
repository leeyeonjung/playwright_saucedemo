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
                echo "[1] 프로젝트 폴더 이동"
                cd $PROJECT_ROOT

                echo "[2] 가상환경 활성화"
                source $VENV

                echo "[3] 패키지 최신화 (optional)"
                pip install --upgrade pip
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                echo "[4] 테스트 실행"
                cd $TEST_DIR

                # 가상환경 python 직접 실행
                /home/ubuntu/saucedemo/saucedemo_pytest/bin/python -m pytest -v || true
                '''
            }
        }

        stage('Collect Latest Report') {
            steps {
                sh '''
                echo "[5] 가장 최근 HTML 리포트 찾기"

                cd $RESULT_DIR

                # 최신 HTML 파일 1개 추출
                LATEST_HTML=$(ls -t *.html | head -n 1)

                echo "가장 최근 리포트: $LATEST_HTML"

                # Jenkins가 읽을 수 있는 workspace로 복사
                cp "$RESULT_DIR/$LATEST_HTML" "$WORKSPACE/"
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
