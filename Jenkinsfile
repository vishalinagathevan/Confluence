pipeline {
    agent any

    environment {
        confUrl = 'https://vishalinagathevan.atlassian.net/wiki/rest/api/content/131199?expand=body.storage'
        appName = 'Test1 RMI Replatform'
    }

    stages {
        stage('Get Services Info') {
            steps {
                script {
                    // Checkout the code
                    checkout scm

                    // Install required Python packages
                    sh 'python -m pip install -r requirements.txt --user'

                    // Run Python script
                    sh "python service-getter.py -u ${confUrl} -a ${appName}"
                }
            }
        }
    }
}