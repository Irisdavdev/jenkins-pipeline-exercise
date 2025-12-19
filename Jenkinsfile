pipeline {
    agent {
        // Ejecutamos dentro de Python 3.9-slim
        docker { image 'python:3.9-slim' }
    }

    // Jenkins revisará GitHub cada 2 minutos
    triggers {
        pollSCM('H/2 * * * *') 
    }

    environment {
        // Credenciales y configuración de BD
        DB_PASS = credentials('postgres-db-password')
        DB_USER = 'postgres'
        DB_NAME = 'cicloturismo'
        DB_HOST = '172.17.0.1' 
        // 🔑 SOLUCIÓN PERMISOS: Instalamos librerías en el workspace del usuario
        PYTHONUSERBASE = "${WORKSPACE}/.pip-modules"
    }

    parameters {
        string(name: 'USUARIO_NOMBRE', defaultValue: 'Estudiante', description: 'Tu nombre')
    }

    stages {
        stage('1. Preparación y Validación') {
            steps {
                script {
                    // 📁 VALIDACIÓN: Verificamos que el setup.sql que creaste en GitHub esté presente
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
                // 🛠️ INSTALACIÓN: Usamos --user para evitar errores de "Permission denied"
                sh 'pip install --user -r requirements.txt'
            }
        }
        stage('3. Ejecución del Reto') {
            steps {
                // Ejecutamos tu script pasando los parámetros necesarios
                // Nota: Asegúrate de que tu archivo se llame 'script.py' o 'main.py'
                sh "python3 script.py ${params.USUARIO_NOMBRE} setup.sql"
            }
        }
    }

    post {
        success {
            echo "✨ ¡Reto completado con éxito, ${params.USUARIO_NOMBRE}!"
        }
        failure {
            echo "❌ Algo salió mal. Revisa el 'Console Output' para más detalles."
        }
    }
}
