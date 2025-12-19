pipeline {
    agent {
        docker { image 'python:3.9-slim' }
    }

    triggers {
        pollSCM('H/2 * * * *') 
    }

    environment {
        DB_PASS = credentials('postgres-db-password')
        DB_USER = 'postgres'
        DB_NAME = 'cicloturismo'
        DB_HOST = '172.17.0.1' 
        PYTHONUSERBASE = "${WORKSPACE}/.pip-modules"
    }

    parameters {
        string(name: 'USUARIO_NOMBRE', defaultValue: 'Estudiante', description: 'Tu nombre')
    }

    stages {
        stage('1. Preparación y Validación') {
            steps {
                script {
                    sh '''
                        if [ -f setup.sql ]; then
                            echo "✅ Archivo setup.sql detectado correctamente."
                        else
                            echo "⚠️ setup.sql no encontrado, creando uno básico..."
                            touch setup.sql
                        fi
                    '''
                    echo "🚀 Entorno listo para ${params.USUARIO_NOMBRE}"
                }
            }
        }
        stage('2. Instalación de Librerías') {
            steps {
                sh 'pip install --user -r requirements.txt'
            }
        }
        stage('3. Ejecución del Reto') {
            steps {
                sh "python3 script.py ${params.USUARIO_NOMBRE} setup.sql"
            }
        }
    }

    post {
        success {
            echo "✅ ¡Felicidades! El script se ejecutó correctamente y la base de datos fue actualizada." 🚴‍♂️
        }
        failure {
            echo "❌ Algo salió mal. Revisa el 'Console Output' para más detalles."
            sh 'rm -f setup.sql'
        }
        always {
            echo "🏁 Finalizando la ejecución del Pipeline de Cicloturismo."
        }
    }
}
