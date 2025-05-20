pipeline {
	agent any

    environment {
		BASE_URL = 'https://recette-front.machallahtravels.com/'
    }

    stages {
		stage('Install dependencies') {
			steps {
				sh 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
			steps {
				sh './jenkins.sh'
            }
        }

        stage('Archive Report') {
			steps {
				archiveArtifacts artifacts: 'report.html', fingerprint: true
            }
        }
    }
}
