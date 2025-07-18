pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                // add your build steps here
            }
        }

        stage('Manual Approval') {
            steps {
                input message: 'Deploy to Production?', ok: 'Proceed'
            }
        }

        stage('Deploy to Production') {
            steps {
                echo 'Starting Django server on port 8001...'

                // Kill any existing python server (optional)
                bat 'taskkill /F /IM python.exe 1>nul 2>&1'

                // Go to the correct directory
                bat 'cd /d C:\\Users\\Deepak\\Futsal-Tournament-Website-Djnago\\futsalWebsite'

                // Start server in background and log output
                bat 'start /B python manage.py runserver 0.0.0.0:8001 > server_8001.log 2>&1'

                // Give it 5 seconds to start
                bat 'timeout /t 5'

                // Optional: Print log output for verification
                bat 'type server_8001.log'

                // Optional: Check if the server is responding
                bat 'powershell -Command "try { (Invoke-WebRequest http://localhost:8001).StatusCode } catch { Write-Output \'Django server not responding\' }"'

                // Optional: Wait for manual testing before Jenkins exits
                bat 'timeout /t 60'
            }
        }
    }
}
