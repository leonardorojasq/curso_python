def saludo():
    nombre_usuario = input("Ingresa tu nombre: ")
    print(f'Hola {nombre_usuario}, Bienvenido!')
        
def edad():
    edad_usuario = input("Ingresa tu edad: ")
    print(f'la edad tuya es: {edad_usuario}')



def menu():
    
  
    while True:
        
        print("######### BIENVENIDO AL MENU #########")
        print("Elije una opción")
        print("1. Saludar")
        print("2. Mostrar Edad")
        print("3. Salir")
       
    
        opcion = int(input("Digita la opcion "))
    
    
        if opcion==1:
            Saludo()
            
        elif opcion==2:
            edad()
            
        elif opcion==3:
            print("Saliendo del Menu...")
            break
        
        else:
            print("Digite un nuemro valido")
            

        
Menu()