pipeline {
    agent any
    environment {
        GIT_REPO = 'https://github.com/CallMeDas/Futsal-Tournament-Website-Djnago.git'
    }
    stages {
        stage('Deploy to Staging') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'github-creds', usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PAT')]) {
                    sh """
                    ssh -o StrictHostKeyChecking=no user@vm1-ip << EOF
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
        }

        stage('Manual Approval') {
            steps {
                input message: 'Deploy to Production?', ok: 'Yes, Deploy'
            }
        }

        stage('Deploy to Production') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'github-creds', usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PAT')]) {
                    sh """
                    ssh -o StrictHostKeyChecking=no user@vm2-ip << EOF
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
}
