pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'your-docker-repo/python-app'
        DOCKER_TAG = "${env.BUILD_NUMBER}"
        KUBE_CONFIG = credentials('kubeconfig')
    }
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/your-repo/python-app.git'
            }
        }
        
        stage('Build') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE}:${DOCKER_TAG} .'
            }
        }
        
        stage('Test') {
            steps {
                sh 'docker run ${DOCKER_IMAGE}:${DOCKER_TAG} python -m pytest'
            }
        }
        
        stage('Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo ${DOCKER_PASS} | docker login -u ${DOCKER_USER} --password-stdin'
                    sh 'docker push ${DOCKER_IMAGE}:${DOCKER_TAG}'
                    sh 'docker tag ${DOCKER_IMAGE}:${DOCKER_TAG} ${DOCKER_IMAGE}:latest'
                    sh 'docker push ${DOCKER_IMAGE}:latest'
                }
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                withKubeConfig([credentialsId: 'kubeconfig']) {
                    sh 'kubectl apply -f kubernetes/'
                    sh 'kubectl set image deployment/python-app python-app=${DOCKER_IMAGE}:${DOCKER_TAG}'
                }
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            slackSend(color: 'good', message: "Build ${env.BUILD_NUMBER} succeeded!")
        }
        failure {
            slackSend(color: 'danger', message: "Build ${env.BUILD_NUMBER} failed!")
        }
    }
}