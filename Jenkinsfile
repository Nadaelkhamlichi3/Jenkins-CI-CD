pipeline {
    agent any

    triggers {
        githubPush()
    }

    environment {
        HOST       = '0.0.0.0'
        PORT       = '5000'
        APP_MODULE = 'app:app'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-token',
                    url: 'https://github.com/Nadaelkhamlichi3/Jenkins-CI-CD.git'
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    pip install pytest-cov
                    python --version
                '''
            }
        }

        stage('Run Tests') {
            parallel {
                stage('Tests app') {
                    steps {
                        sh '''
                            . venv/bin/activate
                            export COVERAGE_FILE=.coverage.app
                            pytest test_app.py --cov=app --cov-report=term
                        '''
                    }
                }
                stage('Tests app 2') {
                    steps {
                        sh '''
                            . venv/bin/activate
                            export COVERAGE_FILE=.coverage.app2
                            pytest test_app_2.py --cov=app --cov-report=term
                        '''
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    . venv/bin/activate
                    JENKINS_NODE_COOKIE=dontKillMe BUILD_ID=dontKillMe \
                    nohup gunicorn --bind ${HOST}:${PORT} ${APP_MODULE} > gunicorn.log 2>&1 &
                '''
            }
        }
    }
}