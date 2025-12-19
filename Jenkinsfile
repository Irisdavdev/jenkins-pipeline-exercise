pipeline {
    agent {
        // Ahora que tienes el plugin, esta sintaxis funcionará perfectamente
        docker { 
            image 'python:3.9-slim' 
        }
    }

    parameters {
        string(name: 'USUARIO_NOMBRE', defaultValue: 'Estudiante', description: 'Introduce tu nombre')
        file(name: 'setup.sql', description: 'Archivo SQL para la base de datos')
    }

    stages {
        stage('1. Preparar Archivos') {
            steps {
                script {
                    // Localizamos el archivo SQL subido y lo movemos al directorio de trabajo
                    // El comando 'find' ayuda a encontrarlo sin importar la carpeta temporal
                    sh "mv \$(find . -name setup.sql) ./setup.sql"
                    echo "✅ Archivo setup.sql listo para el script."
                }
            }
        }

        stage('2. Instalar Dependencias') {
            steps {
                // Dentro del contenedor de Python no necesitas crear un 'venv'
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('3. Ejecutar Script') {
            steps {
                // Pasamos el nombre y el archivo SQL como argumentos
                echo "Ejecutando script para: ${params.USUARIO_NOMBRE}"
                sh "python script.py ${params.USUARIO_NOMBRE} setup.sql"
            }
        }
    }

    post {
        success {
            echo "✅ ¡Felicidades ${params.USUARIO_NOMBRE}! El pipeline se ejecutó correctamente."
        }
        failure {
            echo "❌ Algo salió mal. Verifica que 'requirements.txt' y 'script.py' estén en tu GitHub."
        }
    }
}
