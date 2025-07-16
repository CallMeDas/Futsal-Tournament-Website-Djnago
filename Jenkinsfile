pipeline {
    agent any
    environment {
        VENV = 'venv'
    }
    stages {
        stage('Check Out') {
            steps {
                git branch: 'main', url: 'https://github.com/CallMeDas/Futsal-Tournament-Website-Djnago.git'
            }
        }

        stage('Set up VENV') {
            steps {
                bat 'python -m venv %VENV%'
                bat '%VENV%\\Scripts\\python -m pip install --upgrade pip'
                bat '%VENV%\\Scripts\\pip install -r requirement.txt'
            }
        }

        // stage('Run Django Commands') {
        //     steps {
        //         bat '''
        //             %VENV%\\Scripts\\python tournaments\\manage.py migrate
        //             %VENV%\\Scripts\\python tournaments\\manage.py collectstatic --noinput
        //             %VENV%\\Scripts\\python tournaments\\manage.py test
        //         '''
        //     }
        // }

        stage('Run Server on Port 8000') {
            steps {
                bat '''
                    cd futsalWebsite
                    start /B ..\\%VENV%\\Scripts\\python manage.py runserver 0.0.0.0:8000
                    timeout /T 10
                '''
            }
        }

        stage('Approval') {
            steps {
                input message: "Approve to deploy production server on port 8001?", ok: "Deploy"
            }
        }

                stage('Run Production Server') {
            steps {
                bat '''
                    cd futsalWebsite
                    start /B ..\\%VENV%\\Scripts\\python manage.py runserver 0.0.0.0:8001
                '''
            }
        }


    }
}
