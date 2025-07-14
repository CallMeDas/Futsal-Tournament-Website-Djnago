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

        stage('Run the test') {
            steps {
            bat '''
            cd tournaments
            ..\\venv\\Scripts\\python manage.py migrate
            ..\\venv\\Scripts\\python manage.py collectstatic --noinput
            ..\\venv\\Scripts\\python manage.py test
        '''
            }
        }
    }
}
