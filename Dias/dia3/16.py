# Sistema de tareas PRO:

# agregar,
# listar,
# eliminar por índice,

# validar errores,
# try/except,
# enumerate,


# menú limpio.
# Validadciones
def validar_ingreso(opcion):
    
    if not opcion.isdigit():
        raise ValueError("Debes ingresar dígitos numéricos")
    
    return int(opcion)

#Validar Rango
def validar_rango(opcion):
    if opcion < 1 or opcion > 4:
        raise ValueError("numero fuera del rango, debe estar entre 1 a 4")
    
    
    
# Funciones Crud
def listar_tareas(lista_tareas):
    if not lista_tareas:
        print("No hay tareas para listar")
        return
    else:
        for c, v in enumerate(lista_tareas, start=1):
            print(c, v)


def crear_tareas(lista_tareas):

    tareas = input("Agrega la tarea: ")
    lista_tareas.append(tareas)
    return lista_tareas

def eliminar_tarea(lista_tareas):
    tarea = input("Cual tarea quieres eliminar: ")
    
    try:
        for v in lista_tareas:
            if tarea == v:
                lista_tareas.remove(v)
            else:
                raise ValueError("No existe tu elección vuelve a intentarlo ")
    except ValueError as e:
        print("Error ",e)
    


def menu_tareas():
    lista_tareas = []
    
    while True:
        try:    
            print("#### MENU  #####\n")
            print("Por favor escoja una opción: ")
            print("""
                1 - Listar Tareas\n
                2 - Agregar Tareas\n
                3 - Eliminar Tarea\n
                """)
            print("#########################")
    
            opcion = input("Ingrese una opcion: ")
            # Validad que sea un digito 
            opcion = validar_ingreso(opcion)
            
            
                
            if opcion == 4:
                print("Saliendo del sistema de tareas.")
                break
            
            # Funcion para validar rango de entrada      
            validar_rango(opcion)
                    
            # if de menu
            if opcion == 1:
                listar_tareas(lista_tareas)
                
                
            elif opcion == 2:
                crear_tareas(lista_tareas)             
                
            elif opcion == 3:
                eliminar_tarea(lista_tareas)
            
            
            
        except ValueError as e:
            print("Error ", e)
    
    
    
menu_tareas()