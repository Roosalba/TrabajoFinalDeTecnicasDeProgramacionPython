from database_manager import obtener_conexion

def registrar_producto(nombre,descripcion,cantidad,precio,categoria):
    """
    En el metodo hacemos la conexion, luego hacemos el insert, que
    nos va a ir pidiendo los datos, luego hacemos los cambios, este recibe 
    parametros, que luego lo vamos a usar


    """
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
     """
     El delete colocamos el nombre de nuestra tabla, luego con el
     where que es la condicion, colocamos el id de lo que queremos eliminar
     el delete siempre va con el where, ya que sino lo hacemos eliminariamos 
     todos los datos de nuestra tabla,por  ultimo guardamos los cambios con el commit()
     y cerremos la conexion
     
     
     """
     conexion=obtener_conexion()
     cursor = conexion.cursor()

     cursor.execute('DELETE FROM productos where id =?',(id,))
     filas_afectadas = cursor.rowcount
     conexion.commit()
     conexion.close()
     
     if filas_afectadas >0:
         return True
     else:
         return False

def listar_productos():
    """ Este meteto es de listar, para listar hacemos la conexion
    luego hacemos el select, el cursor va a la bases de datos, luego
    el reslutado hay que guradarlo, usamos el fetchall que nos devuleve
    una lista
    """
    conexion=obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos")
    resultados=cursor.fetchall()
    conexion.close()
    return resultados


def buscar_productos(id):
    """ Este meteto es de buscar es parecido al listar, hacemos la conexion
        luego hacemos el select, el cursor va a la bases de datos, luego
        el reslutado hay que guradarlo, usamos el fetchone que nos devuleve
        una tupla
    """
    conexion=obtener_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?",(id,))
    resultado=cursor.fetchone()
    conexion.close()
    return resultado


def editar_producto(id,nombre,descripcion,cantidad,precio,categoria):
    """
    Para editar, hacemos la conexion con la base de tados, luego
    hacemos la consulta update que se coloca el nombre de la tabla
    luego el set que son los campos que se van a modificar, luego el
    where que es la condicion, que vamos a colocar el Id de los
    datos que queremos modificar, el where es muy importante, sino
    lo colocamos todos los campos de esa tabla se modificarian, por
    ultimo hacemos el conexion.commit(), para guardar los cambios y luego
    cerrar la conexion, es una buena practica cerrar la conexion, 
    para que no tengamos incovenientes

    """
    conexion=obtener_conexion()
    cursor = conexion.cursor()
   
    cursor.execute(
        'UPDATE productos SET nombre =?,descripcion=?,cantidad =?,precio =?,categoria =? WHERE id=?',
        (nombre,descripcion,cantidad,precio,categoria,id) 
    )
                    
    filas_afectadas = cursor.rowcount 
    conexion.commit()
    conexion.close()
    
    if filas_afectadas >0:
        return True
    else:
        return False

     
    