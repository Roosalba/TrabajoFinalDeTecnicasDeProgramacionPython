from database_manager import obtener_conexion

def registrar_producto(nombre,descripcion,cantidad,precio,categoria):

    conexion=obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        '''
        INSERT INTO productos(nombre,descripcion,cantidad,precio,categoria)
        VALUES(?,?,?,?,?)
    ''',
         (nombre,descripcion,cantidad,precio,categoria),        
                   
     )
   
    conexion.commit()
    conexion.close()

def eliminar_producto(id):
     conexion=obtener_conexion()
     cursor = conexion.cursor()

     cursor.execute('DELETE FROM productos where id =?',(id,))
          
     conexion.commit()
     conexion.close()

def listar_productos():
    conexion=obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    resultados=cursor.fetchall()
    conexion.close()
    return resultados


def buscar_productos(id):
    conexion=obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?",(id,))
    resultado=cursor.fetchone()
    conexion.close()
    return resultado


def editar_producto():
    pass
       
       
                    
                    
                    
                

     
    