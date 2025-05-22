pipeline {
	agent any

    environment {
		VENV = '.venv'
    }

    stages {
		stage('Install dependencies') {
			steps {
				echo '🔧 Création de l’environnement virtuel et installation des dépendances'
                bat '''
                    python -m venv %VENV%
                    call %VENV%\\Scripts\\activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Home Page Tests') {
			steps {
				echo '🏠 Exécution des tests de la page d\'accueil'
                bat '''
                    set PYTHONPATH=%cd%
                    call %VENV%\\Scripts\\activate
                    pytest tests\\test_home.py --browser=chrome --headed --html=reports\\home.html --self-contained-html
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
                bat '''
                    set PYTHONPATH=%cd%
                    call %VENV%\\Scripts\\activate
                    pytest tests\\test_reserver.py --browser=chrome --headed --html=reports\\reserver.html --self-contained-html
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
                bat '''
                    set PYTHONPATH=%cd%
                    call %VENV%\\Scripts\\activate
                    pytest tests\\test_transports.py --browser=chrome --headed --html=reports\\transports.html --self-contained-html
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
