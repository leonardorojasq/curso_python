#EJERCICIO 1
#
#Pide una edad.
#
#Mostrar:
#
#mayor de edad,
#menor de edad.

def validar_edad():
    edad = input("Ingrese la edad ")
    
    if edad.isdigit(): #Valido si el ddato ingresado es numero
        edad = int(edad) # Convierto el dato ingresado en un entero
        
        # Validción de edad
        if edad > 0 and edad <= 17:
            print("menor de edad.")
        elif edad >= 18:
            print("mayor de edad.")
    else:
        print("El dato ingresado no es valido. Ingrese una edad valida entre 1 en adelante") #si no esentero saldra este aviso
        
validar_edad()