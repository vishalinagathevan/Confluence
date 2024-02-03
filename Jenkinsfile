pipeline {
    agent any

    environment {
        CONFLUENCE_USERNAME = credentials('CONFLUENCE_USERNAME')
        CONFLUENCE_APITOKEN = credentials('CONFLUENCE_APITOKEN')
    }

    stages {
        stage('Get Services Info') {
            steps {
                script {
                    // Checkout the code
                    checkout scm

                    // Install required Python packages
                    sh 'python -m pip install -r requirements.txt --user'

                    // Define the path to your Python executable
                    def pythonPath = 'C:\\Users\\visha\\AppData\\Local\\Programs\\Python\\Python38\\python.exe'

                    // Define the path to your Python script
                    def pythonScriptPath = 'C:\\Users\\visha\\OneDrive\\Desktop\\Atlassian\\Confluence\\service-getter.py'

                    // Run the Python script with the required arguments
                    def pythonCommand = "${pythonPath} ${pythonScriptPath} -u ${env.CONFLUENCE_USERNAME} -t ${env.CONFLUENCE_APITOKEN} -a ${env.confUrl}"
                    def process = bat(returnStatus: true, script: pythonCommand)

                    // Check the exit status of the Python script
                    if (process != 0) {
                        error "Failed to run the Python script. Exit code: ${process}"
                    }
                }
            }
        }
    }
}