pipeline {
    agent {
        // Ejecutamos todo dentro de un contenedor ligero de Python
        docker { image 'python:3.9-slim' }
    }

    // Punto 8: Jenkins revisará GitHub cada 2 minutos en busca de cambios
    triggers {
        pollSCM('H/2 * * * *') 
    }

    environment {
        // Inyectamos la credencial que creamos
        DB_PASS = credentials('postgres-db-password')
        DB_USER = 'postgres'
        DB_NAME = 'cicloturismo'
        DB_HOST = '172.17.0.1' 
    }

    parameters {
        string(name: 'USUARIO_NOMBRE', defaultValue: 'Estudiante', description: 'Tu nombre')
        file(name: 'setup.sql', description: 'Sube tu archivo SQL')
    }

    stages {
        stage('1. Preparación y Validación') {
            steps {
                script {
                    // Punto 7: Movemos el archivo subido al workspace
                    // Si no se sube nada, 'touch' crea uno vacío para evitar que el script falle
                    sh "mv \$(find . -name setup.sql) ./setup.sql || touch setup.sql"
                    echo "✅ Entorno listo para ${params.USUARIO_NOMBRE}"
                }
            }
        }
        stage('2. Instalación de Librerías') {
            steps {
                // Instalamos psycopg2 y lo que necesite tu script
                sh 'pip install -r requirements.txt'
            }
        }
        stage('3. Ejecución del Reto') {
            steps {
                // Ejecutamos pasando nombre y archivo como argumentos (Puntos 6 y 7)
                sh "python script.py ${params.USUARIO_NOMBRE} setup.sql"
            }
        }
    }

    post {
        success {
            echo "✨ ¡Reto completado con éxito, ${params.USUARIO_NOMBRE}!"
        }
    }
}
