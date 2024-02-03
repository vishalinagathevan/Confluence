import jenkins.model.*
jenkins = Jenkins.instance
node {
    String confUrl = 'https://vishalinagathevan.atlassian.net/wiki/rest/api/content/131199?expand=body.storage'
    String appName = 'Test1 RMI Replatform'
    stage('Get Services Info') {
        checkout scm
        withCredentials([usernamePassword(credentialsId: 'CONFLUENCE', usernameVariable: 'CONFLUENCE_USER', passwordVariable: 'CONFLUENCE_TOKEN')]) {
            bat
            String serviceInfoCommand = """
                python -m pip install -r requirements.txt --user
                python service-getter.py -u ${confUrl} -a ${appName}
            """
            def output = sh(returnStdout: true, script: serviceInfoCommand)
            print(output)
        }
    }
}