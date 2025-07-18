pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/CallMeDas/Futsal-Tournament-Website-Djnago.git'
    }

    stages {
        stage('Clone Repo') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'github-creds', usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PAT')]) {
                    sh '''
                    rm -rf webapp || true
                    git clone https://${GIT_USER}:${GIT_PAT}@github.com/CallMeDas/Futsal-Tournament-Website-Djnago.git webapp
                    '''
                }
            }
        }

        stage('Deploy to Staging') {
            steps {
                sh '''
                pkill -f "python3 manage.py runserver" || true
                cd webapp
                pip3 install -r requirement.txt
                nohup python3 manage.py runserver 0.0.0.0:8000 > app.log 2>&1 &
                '''
            }
        }

        stage('Manual Approval') {
            steps {
                input message: 'Deploy to Production?'
            }
        }

        stage('Deploy to Production') {
            steps {
                sh '''
                pkill -f "python3 manage.py runserver" || true
                cd webapp
                nohup python3 manage.py runserver 0.0.0.0:8001 > prod.log 2>&1 &
                '''
            }
        }
    }
}
