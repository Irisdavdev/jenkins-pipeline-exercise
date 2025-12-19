pipeline {

    agent any

    parameters {
        string(name: 'USUARIO_NOMBRE', defaultValue: 'Estudiante', description: 'Introduce tu nombre')
        file(name: 'setup.sql', description: 'Archivo SQL para la base de datos')
    }

    stages {
        stage('1. Verificar Python') {
            steps {
                script {
                    // Este comando busca python3 en las rutas comunes automáticamente
                    def pythonPath = sh(script: "which python3 || which python", returnStdout: true).trim()
                    echo "🐍 Python encontrado en: ${pythonPath}"
                    
                    // Guardamos la ruta para usarla después
                    env.PYTHON_EXE = pythonPath
                }
            }
        }

        stage('2. Crear entorno virtual') {
            steps {
                // Usamos la variable que acabamos de encontrar
                sh "${env.PYTHON_EXE} -m venv venv"
                echo "Entorno virtual creado correctamente"
            }
        }

        stage('3. Instalar requirements.txt') {
            steps {
                // Punto 3: Instalar dependencias
                sh './venv/bin/pip install --upgrade pip'
                sh './venv/bin/pip install -r requirements.txt'
                echo "Dependencias instaladas"
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
