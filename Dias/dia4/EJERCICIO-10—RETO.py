# EJERCICIO 10 — RETO

# CRUD PRO de usuarios:

# 1. Crear usuario
# 2. Listar usuarios
# 3. Buscar usuario
# 4. Actualizar usuario
# 5. Eliminar usuario
# 6. Salir

# Debe usar:

# listas,
# diccionarios,
# funciones,
# try/except,
# raise,
# validaciones.


# VALIDACIONES
def verificar_int(opcion):
    if not opcion.isdigit():
        raise ValueError("La opción seleccionada no valida!")
    
    return int(opcion)
    
# FUNCIONES CRUD
def crear_usuario(lista):
       
    crear_usuario = input("Ingrese el nombre usuario a crear: ")
    
    if not crear_usuario:
        raise ValueError("Debes agregar un usuario")
    
    if crear_usuario.isdigit():
        raise ValueError("No debe agregar números ya que solo se admiten nombres!.")
    
    lista.append(crear_usuario)
    print("Usuario creado existosamente!")
    

def listar_usuarios(lista):
    if not lista:
        raise ValueError("No hay datos para mostrar")
    
    if lista:
        print("\nLISTADO DE USUARIOS\n")
    
    for clave, valor in enumerate(lista, start=1):
        print(clave,valor)


def buscar_usuario(lista):
    
    buscar = input("Ingrese el nombre: ")
    
    if buscar.isdigit():
        raise ValueError("No ingreses numeros, ingresa un nombre")
    
    if buscar in lista:
        print("Lo hemos encontrado ",buscar)
    else:
        print("Lo sentimos el usuario no hace parte de nuestra bd")

def actualizar_usuario(lista):
    if not lista:
        raise ValueError("No ingresate ningun nombre.")
    
    
    for clave, valor in enumerate(lista, start=1):
        print(clave, valor)
    
    
    buscar = input("Ingresa el indice a actualizar: ")
    
    if not buscar.isdigit():
        raise ValueError("Ingresa solo el numero del indic para actualizar")
    
    buscar = int(buscar)
    
    if buscar < 1 or buscar > len(lista):
        raise ValueError(
            "Índice fuera de rango"
        )

    
    nuevo_nombre = input("ingrese el nuevo nombre: ").strip()
    if nuevo_nombre.isdigit():
        raise ValueError("Ingresa solo el nombre para ser actualizado")
    
    lista[buscar - 1] = nuevo_nombre
    
    print("Usuario actualizado corerctamente")
    
def eliminar_usuario(lista):
    if not lista:
        raise ValueError("No ingresate ningun nombre.")
    
    for clave, valor in enumerate(lista, start=1):
        print(clave, valor)
    
    
    buscar = input("Ingresa el indice a actualizar: ")
    
    if buscar < 1 or buscar > len(lista):
        raise ValueError(
            "Índice fuera de rango"
        )
    
    if not buscar.isdigit():
        raise ValueError("Ingresa solo el numero del indic para actualizar")
    
    buscar = int(buscar)
        
    lista.pop(buscar - 1)
    print("Usuario eliminado")
    


def usuario():
    lista = [] 
    
    while True:
        try:
            print("###############################")
            print("Escoje una opción")
            print("""
            1. Crear usuario\n
            2. Listar usuarios\n
            3. Buscar usuario\n
            4. Actualizar usuario\n
            5. Eliminar usuario\n
            6. Salir\n
            """)
            print("###############################")

    
            opcion = input("Ingrese una opción: ")
            
            verificar_int(opcion)
            opcion = verificar_int(opcion)
            
            if opcion < 1 or opcion > 6:
                raise ValueError("La opción no debe estar por debajo de 1 ni superior a 5")
                
            
            if opcion == 6:
                print("Saliendo...")
                break
            
            if opcion == 1:
                crear_usuario(lista)
                
            elif opcion == 2:
                listar_usuarios(lista)
                
            elif opcion == 3:
                buscar_usuario(lista)
                
            elif opcion == 4:
                actualizar_usuario(lista)
                
            elif opcion == 5:    
                 eliminar_usuario(lista)
                
        
        except ValueError as e:
            print(e)

usuario()