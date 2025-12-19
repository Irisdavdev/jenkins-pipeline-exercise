pipeline {
    // Usamos un contenedor de Python para que no dependa de lo que hay instalado en el servidor
    agent {
        docker { 
            image 'python:3.9-slim' 
        }
    }

    parameters {
        string(name: 'USUARIO_NOMBRE', defaultValue: 'Estudiante', description: 'Introduce tu nombre')
        // Punto 7: Parámetro de archivo para el SQL
        file(name: 'setup.sql', description: 'Sube tu archivo setup.sql')
    }

    stages {
        stage('1. Preparar Archivos') {
            steps {
                script {
                    // Jenkins guarda los archivos subidos en una ruta temporal. 
                    // Debemos moverlo al workspace para que el script de Python lo vea.
                    sh "mv \$(find . -name setup.sql) ./setup.sql"
                    echo "✅ Archivo SQL preparado en el workspace"
                }
            }
        }

        stage('2. Instalar Dependencias') {
            steps {
                // En un contenedor Docker de Python, no solemos necesitar venv,
                // podemos instalar directamente en el sistema del contenedor.
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('3. Ejecución del Script') {
            steps {
                // Punto 7: Pasamos el nombre y el archivo SQL como argumentos al script
                echo "Ejecutando proceso para: ${params.USUARIO_NOMBRE}"
                sh "python script.py ${params.USUARIO_NOMBRE} setup.sql"
            }
        }
    }

    post {
        success {
            echo "✅ ¡Felicidades ${params.USUARIO_NOMBRE}! El reto se completó con éxito."
        }
        failure {
            echo "❌ Hubo un error. Revisa si el archivo requirements.txt existe en tu repo."
        }
    }
}
