pipeline {
	agent any

    environment {
		VENV = '.venv'
    }

    stages {
		stage('Install dependencies') {
			steps {
				echo '🔧 Création de l’environnement et installation des dépendances'
                sh '''
                    python3 -m venv ${VENV}
                    source ${VENV}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Set PYTHONPATH') {
			steps {
				echo '📁 Définir PYTHONPATH'
                sh 'export PYTHONPATH=$(pwd)'
            }
        }

        stage('Run Home Page Tests') {
			steps {
				echo '🏠 Tests de la page d\'accueil'
                sh '''
                    source ${VENV}/bin/activate
                    pytest tests/test_home.py --browser=chrome --headed --html=reports/home.html --self-contained-html
                '''
            }
            post {
				always {
					archiveArtifacts artifacts: 'reports/home.html', fingerprint: true
                }
            }
        }

        stage('Run Reservation Form Tests') {
			steps {
				echo '📝 Tests du formulaire de réservation'
                sh '''
                    source ${VENV}/bin/activate
                    pytest tests/test_reserver.py --browser=chrome --headed --html=reports/reserver.html --self-contained-html
                '''
            }
            post {
				always {
					archiveArtifacts artifacts: 'reports/reserver.html', fingerprint: true
                }
            }
        }

        stage('Run Transports Page Tests') {
			steps {
				echo '🚌 Tests de la page transports'
                sh '''
                    source ${VENV}/bin/activate
                    pytest tests/test_transports.py --browser=chrome --headed --html=reports/transports.html --self-contained-html
                '''
            }
            post {
				always {
					archiveArtifacts artifacts: 'reports/transports.html', fingerprint: true
                }
            }
        }
    }

    post {
		always {
			echo '✅ Pipeline terminé. Vérifiez les rapports HTML.'
        }
    }
}
