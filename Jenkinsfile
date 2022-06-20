pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'python -V'
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
            }
        }
    }
}
