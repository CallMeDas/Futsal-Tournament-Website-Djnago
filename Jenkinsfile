pipeline {
    agent any
    environment {
        GIT_REPO = 'https://github.com/CallMeDas/Futsal-Tournament-Website-Djnago.git'
        GIT_USER = 'callmedas'
        GIT_PAT = credentials('github-pat-token') // Store PAT in Jenkins credentials
    }
    stages {
        stage('Deploy to Staging') {
            steps {
                sh """
                ssh user@vm1-ip << EOF
                    pkill -f "manage.py runserver" || true
                    rm -rf webapp || true
                    git clone https://${GIT_USER}:${GIT_PAT}@github.com/CallMeDas/Futsal-Tournament-Website-Djnago.git webapp
                    cd webapp
                    pip3 install -r requirement.txt
                    nohup python3 manage.py runserver 0.0.0.0:8000 > app.log 2>&1 &
                EOF
                """
            }
        }

        stage('Manual Approval') {
            steps {
                input message: 'Deploy to Production?'
            }
        }

        stage('Deploy to Production') {
            steps {
                sh """
                ssh user@vm2-ip << EOF
                    pkill -f "manage.py runserver" || true
                    rm -rf webapp || true
                    git clone https://${GIT_USER}:${GIT_PAT}@github.com/CallMeDas/Futsal-Tournament-Website-Djnago.git webapp
                    cd webapp
                    pip3 install -r requirement.txt
                    nohup python3 manage.py runserver 0.0.0.0:8001 > app.log 2>&1 &
                EOF
                """
            }
        }
    }
}
