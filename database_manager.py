import sqlite3
from colorama import Fore, Style, init


# Hago la conexion
def obtener_conexion():
    conexion= sqlite3.connect("inventario.db")
    return conexion

# Creo la funcion para crear la tabla
def crear_tabla():
    # llamo  a la funcion de arriba
    conexion=obtener_conexion()
    cursor = conexion.cursor()


    cursor.execute("""

        CREATE TABLE IF NOT EXISTS productos(
            id INTEGER PRIMARY KEY  AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            cantidad INTEGER NOT NULL,
            precio REAL NOT NULL,
            categoria TEXT

                   )

""")
    
    conexion.commit()# Aqui guardamos los cambios
    conexion.close()# Cerremos la conexion

print("La tabla productos creada con exito")

if __name__ == "__main__":
    crear_tabla()