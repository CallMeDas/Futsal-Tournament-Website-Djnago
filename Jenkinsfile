pipeline{
    agent any
    environment{
        VENV = 'venv'
    }
    stages{
        stage('check out'){
            steps{
                git branch: 'main', url: 'https://github.com/CallMeDas/Futsal-Tournament-Website-Djnago.git'
            }
        }
        stage('Set up VENV'){
            steps{
                bat 'python -m venv %VENV%'
                bat '%VENV%\\Scripts\\python -m install --upgrade pip'
                bat '%VENV%\\Scripts\\pip install -r requirement.txt'
            }

        }
        stage('Run the test'){
            steps{
                bat '%VENV%\\Scripts\\python manage.py test'
            }
        }
    }
}
