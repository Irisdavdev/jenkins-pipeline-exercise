import os
import sys
import psycopg2

def run_script():
    # Punto 6: Capturar el nombre enviado desde Jenkins
    # sys.argv[0] es el nombre del script, sys.argv[1] será el primer parámetro
    nombre_usuario = sys.argv[1] if len(sys.argv) > 1 else "Usuario Desconocido"
    print(f"--- Iniciando script para: {nombre_usuario} ---")

    # Variables de entorno (Punto 1)
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_NAME = os.getenv('DB_NAME', 'cicloturismo')
    DB_USER = os.getenv('DB_USER', 'postgres')
    DB_PASS = os.getenv('DB_PASS', 'postgres')

    # Punto 7: Podríamos pasar la ruta del SQL como segundo parámetro
    sql_file = sys.argv[2] if len(sys.argv) > 2 else 'setup.sql'

    try:
        print(f"Conectando a la base de datos en {DB_HOST}...")
        conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASS)
        cur = conn.cursor()

        print(f"Leyendo archivo: {sql_file}")
        with open(sql_file, 'r') as f:
            sql = f.read()
            cur.execute(sql)

        conn.commit()
        cur.close()
        conn.close()
        print(f"✅ SQL ejecutado correctamente. ¡Buen trabajo, {nombre_usuario}!")
        
    except FileNotFoundError:
        print(f"❌ Error: No se encontró el archivo {sql_file}")
        sys.exit(1) # Indicamos a Jenkins que el stage falló
    except Exception as e:
        print(f"❌ Error de conexión o ejecución: {e}")
        sys.exit(1) 

if __name__ == "__main__":
    run_script()
    