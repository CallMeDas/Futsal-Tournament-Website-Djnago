pipeline {
    agent any

    environment {
        GIT_REPO = 'https://github.com/CallMeDas/Futsal-Tournament-Website-Djnago.git'
    }

    stages {
        stage('Clone Repo') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'github-creds', usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PAT')]) {
                    bat '''
                    if exist webapp (rmdir /s /q webapp)
                    git clone https://%GIT_USER%:%GIT_PAT%@github.com/CallMeDas/Futsal-Tournament-Website-Djnago.git webapp
                    '''
                }
            }
        }

        stage('Deploy to Staging') {
            steps {
                bat '''
                taskkill /F /IM python.exe > nul 2>&1
                cd webapp\\futsalWebsite
                pip install -r ..\\requirement.txt
                start /B python manage.py runserver 0.0.0.0:8000
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
                bat '''
                taskkill /F /IM python.exe > nul 2>&1
                cd webapp\\futsalWebsite
                start /B python manage.py runserver 0.0.0.0:8001
                '''
            }
        }
    }
}
