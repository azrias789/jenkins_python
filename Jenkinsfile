pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python -V'
		sh 'hostname'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'python3 -V'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
		sh 'df'
                sh 'git pull https://github.com/hanley/jenkins_python.git'
                sh 'ls -la jenkins_python'
                sh 'python jenkins_python/cal.py'
            }
        }
    }
}
