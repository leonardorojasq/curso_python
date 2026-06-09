#EJERCICIO 5
#
#Sumar todos los números de una lista.
#
#RETO IMPORTANTE
#
#Sistema de tareas:
#
#1. Agregar tarea
#2. Ver tareas
#3. Eliminar tarea
#4. Salir
#
#Debe:
#
#usar lista,
#usar while,
#usar funciones,
#validar errores,
#no explotar.

def listar(tareas):
    if not tareas:
        print("No hay tareas para listar")
    else:
        for indice, nombre in enumerate(tareas, start=1):
            print(indice, nombre)
    

def crear(tareas):
    tarea = input("Ingrese la tarea: ")
    tareas.append(tarea)
    
    
def remover(tareas):
    if not tareas:
        print("No hay tareas para eliminar")
    
    else:
        tareas.pop()
    


def tareas():
    tareas = []
    
    while True:
        try:
            print("Sistema de tareas")
            print("Elije la opcion de tu preferencia.\n")
            
            opcion = input("Ingrese la opcion: ")
            
            if not opcion.isdigit():
                print("Debes ingresar un numero")
                continue
            
            opcion = int(opcion)
            
                       
            if opcion == 4:
                print("Saliendo...")
                break
            
            if opcion < 1 or opcion  > 5:
                print("La opción ingresada no es valida")
                continue
                           
                            
            if opcion == 1:
                listar(tareas)
                
            if opcion == 2:
                crear(tareas)
                
            if opcion == 3:                
                remover(tareas)
           
                
                
                
            
            
            
            
            
        except:
            print("Error")
    
    
tareas()