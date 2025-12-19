pipeline {
    agent any

    parameters {
        string(name: 'USUARIO_NOMBRE', defaultValue: 'Estudiante', description: 'Introduce tu nombre')
        // Añadimos el parámetro de archivo para el punto 7
        file(name: 'setup.sql', description: 'Archivo SQL para la base de datos')
    }

    environment {
        // Punto 1: Variable definida por el usuario
        MI_VAR_USUARIO = "Ejecución de Ejercicio"
    }

    stages {
        stage('1. Información Inicial') {
            steps {
                // Punto 1: Print de información básica y globales
                echo "--- Datos de la Ejecución ---"
                echo "Usuario que ejecuta: ${params.USUARIO_NOMBRE}"
                echo "ID de Construcción: ${env.BUILD_ID}"
                echo "Nombre del Job: ${env.JOB_NAME}"
                echo "Variable de usuario: ${env.MI_VAR_USUARIO}"
            }
        }

        stage('2. Crear entorno virtual') {
            steps {
                // Punto 2: Crear venv
                sh 'python3 -m venv venv'
            }
        }

        stage('3. Instalar requirements.txt') {
            steps {
                // Punto 3: Instalar dependencias
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
            }
        }

        stage('4. Ejecutar script') {
            steps {
                // Punto 4 y 6: Ejecutar script pasando el parámetro de nombre
                echo "Ejecutando script para: ${params.USUARIO_NOMBRE}"
                sh "./venv/bin/python script.py ${params.USUARIO_NOMBRE}"
            }
        }
    }

    // Punto 9: Configuración según el resultado del pipeline
    post {
        success {
            echo "✅ ¡Felicidades ${params.USUARIO_NOMBRE}! El pipeline salió bien."
        }
        failure {
            echo "❌ Algo falló en la ejecución. Revisa los logs de la consola."
        }
    }
}
