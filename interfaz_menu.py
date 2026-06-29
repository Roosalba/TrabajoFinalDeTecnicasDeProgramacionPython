from colorama import Fore, Style, init
import captura_datos

init(autoreset=True)

def menu():
    print(f"\n{Fore.BLUE}=== GESTIÓN DE INVENTARIO ===")
    print("1.Registrar productos ")
    print("2.Listar productos ")
    print("3.Buscar productos ")
    print("4.Borrar productos")
    print("5.Editar productos")
    print("6.Salir")


def principal():
    while True:
        menu()
        opcion=input(f"\n{Fore.YELLOW}Seleccione una opción (1-6): {Style.RESET_ALL}").strip()

        if opcion=="":
            print("El campo no puede estar vacio")
            continue
                
        elif opcion =="1":
            print(f"\n{Fore.GREEN}--- Registrar Nuevo Producto ---")
            while True:
                nombre=str(input("Ingrese el nombre del producto: "))
                if nombre=="":
                    print("El nombre no puede estar vacio")
                    continue
                break
            while True:
                descripcion=str(input("Ingrese la descripcion del producto: "))
                if descripcion=="":
                    print("La descripcion no puede estar vacia")
                    continue
                break
            while True:
                try:
                    cantidad=int(input("Ingrese la cantidad (Entero): "))
                    if cantidad <0:
                        print("La cantidad no puede ser negativa")
                        continue

                    break 

                except ValueError:
                    print(f"{Fore.RED}Error: La cantidad debe ser un número entero")
                          
            while True:
                try:
                    precio=float(input("Ingrese el precio (Decimal): "))
                    if precio < 0:
                        print("El precio no puede ser negativo")
                        continue
                    break
                except ValueError:
                    print(f"{Fore.RED}Error: el precio debe ser un número decimal")
            while True:
                    categoria=str(input("Ingrese la categoria: "))
                    if categoria=="":
                        print("La categria no puede estra vacia")
                        continue
                    break
            captura_datos.registrar_producto(nombre,descripcion,cantidad,precio,categoria)
            print(f"\n{Fore.GREEN}¡Producto registrado con éxito!")


        elif opcion=="2":
            print(f"\n{Fore.GREEN}--- Listar los Productos ---")
            resultados=captura_datos.listar_productos()

            if not resultados:
                print("No hay productos para mostrar")
            else:
                for produ in resultados:
                    print(f"ID:{produ[0]} NOMBRE:{produ[1]}  DESCRIPCION:{produ[2]}  CANTIDAD:{produ[3]}  PRECIO:{produ[4]} CATEGORIA:{produ[5]}")
                         
        elif opcion=="3" :    
             print(f"\n{Fore.GREEN}--- Buscar  Productos ---")
             while True:
                 
                try:
                    buscar_producto=int(input("Ingrese el id del producto a buscar: "))
                    if buscar_producto==0:
                        break
                   
                    produ=captura_datos.buscar_productos(buscar_producto)
                    if not produ:
                       print(f"{Fore.RED}No se encontró el producto con ese ID.")
                       
                    else:
                        print(f"ID:{produ[0]} NOMBRE:{produ[1]}  DESCRIPCION:{produ[2]}  CANTIDAD:{produ[3]}  PRECIO:{produ[4]} CATEGORIA:{produ[5]}")
                        break
                except ValueError:
                    print(f"{Fore.RED}Error: debe ingresar un numero")
                

        elif opcion=="4":
             print(f"\n{Fore.GREEN}--- Eliminar  Productos ---")
             while True:
                try:
                    id_eliminar=int(input("Ingrese el ID del producto a eliminar: "))
                    if id_eliminar==0:
                        break
                    eliminado_exitoso=captura_datos.eliminar_producto(id_eliminar)
                     
                    if not eliminado_exitoso:
                        print(f"{Fore.RED}No existe ningún producto con el ID {id_eliminar}. Intente de nuevo.")
                        
                    else:
                        print(f"{Fore.GREEN}¡Producto eliminado con éxito!")
                        break      
                except ValueError:
                    print(f"{Fore.RED}Error: debe ingresar un numero")
                   
        elif  opcion =="5":
           
            print(f"\n{Fore.GREEN}--- Editar Productos ---")
            
            # para validar id
            while True:
                try:
                    id_editar = int(input("Ingrese el ID del producto que desea editar (o 0 para regresar): "))
                    if id_editar == 0:
                        break # El usuario decidió cancelar
                    
                    # Usamos el metodo buscar_productos para buscar el producto
                    existe = captura_datos.buscar_productos(id_editar)

                    if existe: 
                        break # Si encuentra el ID, Rompemos este bucle y avanza para pedir los datos, sno se esjecuta el else
                    else:
                        print(f"{Fore.RED}Error: El ID {id_editar} no existe en la base de datos. Intente de nuevo.")
                        
                except ValueError:
                    print(f"{Fore.RED}Error: El ID debe ser un número entero.")
            
            
            if id_editar == 0:
                continue

            
            # Si el programa llega aqui el ID fue validado
           
            print(f"\n{Fore.CYAN}Ingrese los nuevos datos para el producto:")
            
            while True:
                nuevo_nombre = input("Nuevo Nombre: ").strip()
                if nuevo_nombre: break
                print(f"{Fore.RED}El nombre no puede estar vacío.")

            while True:
                descripcion = input("Nueva Descripción: ").strip()
                if descripcion: break
                print(f"{Fore.RED}La descripción no puede estar vacía.")

            while True:
                try:
                    cantidad = int(input("Nueva Cantidad (Entero): "))
                    if cantidad >= 0: break
                    print(f"{Fore.RED}La cantidad no puede ser negativa.")
                except ValueError:
                    print(f"{Fore.RED}Debe ser un número entero.")

            while True:
                try:
                    precio = float(input("Nuevo Precio (Decimal): "))
                    if precio >= 0: break
                    print(f"{Fore.RED}El precio no puede ser negativo.")
                except ValueError:
                    print(f"{Fore.RED}Debe ser un número decimal.")

            while True:
                categoria = input("Nueva Categoría: ").strip()
                if categoria: break
                print(f"{Fore.RED}La categoría no puede estar vacía.")

            # Guardamos los cambios llamando al  metodo de editar
            if captura_datos.editar_producto(id_editar, nuevo_nombre, descripcion, cantidad, precio, categoria):
                print(f"\n{Fore.GREEN}¡Producto editado con éxito!")
            else:
                print(f"\n{Fore.RED}Error al guardar los cambios.")
        elif opcion=="6":
            print("Fin del programa")
            break

        else:
            print("Opcion incorrecta")

if __name__ == "__main__":
    principal()