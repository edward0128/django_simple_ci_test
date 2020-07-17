pipeline {
    agent any
    stages {
        stage('Gitlab (pull code frome gitlab)') {
            steps {
                sh 'echo "start to clone code"'
            }

        }
        stage('Build (Bu)') {
            steps {
                git 'https://github.com/edward0128/django_simple_ci_test.git'
                sh 'docker ps'
                sh 'docker login --username=yusongwang1991 --password=reborn7777'
                sh 'cd DockerBuild && docker build -t yusongwang1991/django_simple_ci_test:latest .'
                sh 'docker push yusongwang1991/django_simple_ci_test:latest'

            }

        }
        stage('Release') {
            steps {
                sh 'echo "start to push to docker"'
            }

        }
        stage('Deploy') {
            steps {
                sh 'echo "Star to deploy to k8s"'
            }

        }        
        stage('Test') {
            steps {
                sh 'echo "Star to test web"'
            }

        }
    }
}

