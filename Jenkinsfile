pipeline {
    agent any
    environment {
        DOCKERHUB_USER = 'vijaybharathg0405'
        DOCKERHUB_PASS = 'GvijayB@0405' 
        IMAGE_TAG = "${env.GIT_COMMIT}"
    }
    stages {
        stage('Source & Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Continuous Integration') {
            steps {
                // Using Windows batch commands since your Jenkins runs on Windows
                bat 'python -m pip install --upgrade pip'
                bat 'pip install -r requirements.txt'
                bat 'pytest test_app.py'
            }
        }
        stage('Build & Push Docker Image') {
            steps {
                script {
                    bat "docker build -t ${DOCKERHUB_USER}/library-app:${IMAGE_TAG} ."
                    bat "echo ${DOCKERHUB_PASS} | docker login -u ${DOCKERHUB_USER} --password-stdin"
                    bat "docker push ${DOCKERHUB_USER}/library-app:${IMAGE_TAG}"
                }
            }
        }
        stage('Deployment Manifest Prep') {
            steps {
                // Powershell replacement logic for Windows runner nodes
                bat "powershell -Command \"(Get-Content k8s-deployment.yml) -replace 'IMAGE_TAG', '${IMAGE_TAG}' | Set-Content k8s-deployment.yml\""
                bat "type k8s-deployment.yml"
            }
        }
    }
}