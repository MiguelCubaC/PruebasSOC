import sqlite3
# Defininiendo las credenciales de prueba para el acceso a la base de datos PACIFICOTEST
DB_NAME = 'pacificodigital.db'
USERNAME = 'usuarioPrueba'
PASSWORD = 'passwordPrueba'

try:
    # Conectar a la base de datos
    conn = sqlite3.connect(DB_NAME)

    # Autenticar con las credenciales
    cursor = conn.cursor()
    cursor.execute("PRAGMA user_version = 1")  # Ejemplo de consulta para verificar la autenticación
    print("Autenticación exitosa.")

    # Aquí puedes ejecutar consultas, modificaciones, etc.

except sqlite3.Error as e:
    print("Error al conectar a la base de datos:", e)

finally:
    # Cerrar la conexión
    if conn:
        conn.close()
# PACIFICO PORTAL DE PRUEBA
com.pacifico.portal.prueba.key == '312312sdasd23123123sdasd'
com.pacificoseguros.portal.prueba.key == '312312sdasd23123123sdasd'
com.primaafp.portal.prueba.key == 'dsfdscxc23sdsfsfsdffdgg'