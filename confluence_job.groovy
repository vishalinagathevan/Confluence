pipeline {
    agent any

    options {
        buildDiscarder(logRotator(artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: ''))
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout your source code repository
                git 'https://github.com/vishalinagathevan/Confluence.git'
            }
        }

        stage('Confluence Page Job') {
            steps {
                // Execute the Python script
                script {
                    sh 'python confluence_page.py -confluence_api_base https://vishalinagathevan.atlassian.net/wiki/rest/api/content/131199?expand=body.storage -app_name "Test1 RMI Replatform"'
                }
            }
        }
    }

    post {
        always {
            // Add any cleanup or final steps here
        }
    }
}