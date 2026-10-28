pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials-id') // Must match your Jenkins Credentials ID
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
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
                sh 'pytest test_app.py'
            }
        }
        stage('Build & Push Docker Image') {
            steps {
                script {
                    sh "docker build -t vijaybharath04/library-app:${IMAGE_TAG} ."
                    withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials-id', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                        sh "echo \$PASS | docker login -u \$USER --password-stdin"
                        sh "docker push vijaybharath04/library-app:${IMAGE_TAG}"
                    }
                }
            }
        }
        stage('Deployment Manifest Prep') {
            steps {
                sh "sed -i 's/IMAGE_TAG/${IMAGE_TAG}/g' k8s-deployment.yml"
                sh "cat k8s-deployment.yml"
            }
        }
    }
}