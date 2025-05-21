pipeline {
	agent any

    environment {
		PYTHONPATH = "${env.WORKSPACE}"
    }

    stages {
		stage('Exécution du script Jenkins') {
			steps {
				echo '🚀 Exécution du script jenkins.sh'
                bat 'jenkins.sh'
            }
        }

        stage('Archivage rapport') {
			steps {
				echo '📦 Archivage du rapport HTML généré'
                archiveArtifacts artifacts: 'reports/report.html', allowEmptyArchive: true
            }
        }
    }

    post {
		always {
			echo '🧹 Nettoyage du workspace'
            deleteDir()
        }
    }
}
