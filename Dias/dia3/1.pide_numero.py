

def pedir_numero():
    try:
        numero_ingresado = int(input("Ingresa el numero: "))
        print(f'El numero es {numero_ingresado}')
        
    except:
        print("El dato ingresado no es valido")
    
pedir_numero()





