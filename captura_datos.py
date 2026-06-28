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
     filas_afectadas = cursor.rowcount
     conexion.commit()
     conexion.close()
     
     if filas_afectadas >0:
         return True
     else:
         False

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


def editar_producto(id,nombre,descripcion,cantidad,precio,categoria):
    conexion=obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute('UPDATE productos SET nombre =?,descripcion=?,cantidad =?,precio =?,categoria =? WHERE id=?'
                   
      (nombre,descripcion,cantidad,precio,categoria,id) )
                   
    filas_afectadas = cursor.rowcount # pára mirar las filas que fueron afectadas
    conexion.commit()
    conexion.close()
    if filas_afectadas >0:
        return True
    else:
        False              
                    
                    
                

     
    