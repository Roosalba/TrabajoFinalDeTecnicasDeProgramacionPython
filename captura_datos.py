from database_manager import obtener_conexion




def registrar_producto():
    
    conexion=obtener_conexion()
    cursor = conexion.cursor()