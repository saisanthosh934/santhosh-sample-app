pipeline{
    agent any
    stages{
        stage("Checkout"){
            steps{
                git branch: 'main', url: 'https://github.com/saisanthosh934/santhosh-sample-app'
            }
            
        }

        
        stage('Docker Image Build') {
            steps {
                script {
                        sh 'docker system prune -f'
                        sh 'docker container prune -f'
                        sh 'docker build -t ${APP_NAME}:${BUILD_NUMBER} .'
                }
            }
        }
        
        stage('Test') {
            steps {
                 sh 'docker run python-app:${BUILD_NUMBER} python -m pytest || [ $? -eq 5 ] && echo "No tests found"'
            }
        }
        
        stage('Docker Image Push') {
            steps {
            withCredentials([usernamePassword(credentialsId: 'docker-credentials-id', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
            script {
                sh 'ls -la'
                sh 'pwd'
                sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                sh 'docker tag ${APP_NAME}:${BUILD_NUMBER} ${DOCKER_USERNAME}/${APP_NAME}:${BUILD_NUMBER}'
                sh 'docker push ${DOCKER_USERNAME}/${APP_NAME}:${BUILD_NUMBER}'
                sh 'docker logout'
            }
            }
            }
        }

        
        
    }
    post{
        always{
            echo "========always========"
        }
        success{
            echo "========pipeline executed successfully ========"
        }
        failure{
            echo "========pipeline execution failed========"
        }
    }
}