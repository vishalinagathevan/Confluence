node {
    String confUrl = 'https://vishalinagathevan.atlassian.net/wiki/rest/api/content/131199?expand=body.storage'
    String appName = 'Test1 RMI Replatform'
    // stage('Get Services Info') {
        checkout scm
        withCredentials([usernamePassword(credentialsId: 'CONFLUENCE', usernameVariable: 'CONFLUENCE_USER', passwordVariable: 'CONFLUENCE_TOKEN')]) {
            String serviceInfoCommand = """
                python -m pip install -r requirements.txt --user
                python service-getter.py -u ${confUrl} -a ${appName}
            """
            def output = sh(returnStdout: true, script: serviceInfoCommand)
            print(output)
        }
    // }

    stage('Get Services Info') {
    checkout scm
    withCredentials([usernamePassword(credentialsId: 'CONFLUENCE', usernameVariable: 'CONFLUENCE_USER', passwordVariable: 'CONFLUENCE_TOKEN')]) {
        script {
            sh 'python -m pip install -r requirements.txt --user'
            sh "python service-getter.py -u ${confUrl} -a ${appName}"
        }
    }
}
}