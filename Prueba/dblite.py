import sqlite3

with sqlite3.connect('mi_base_de_datos.db') as conexion:
    cursor = conexion.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nombre TEXT)")
    cursor.execute("INSERT INTO usuarios (nombre) VALUES ('Alice')")
    conexion.commit()