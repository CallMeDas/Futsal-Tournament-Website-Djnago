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
    }
}
