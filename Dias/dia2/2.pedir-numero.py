#EJERCICIO 2
#
#Pide un número.
#
#Mostrar:
#
#positivo,
#negativo,
#o cero.

def validar_signo_numero():
    
    numero = input("Ingrese un numero para validar el signo ")
    
    if numero.lstrip("-").isdigit():
        numero = int(numero)
        
        if numero < 0:
            print("El numero ingresado es negativo")
        
        elif numero == 0:
            print("El numero ingresado es 0(cero)")
        else:
            print("El numero ingresado es un numero positivo")
    
    else:
        print("El caracter ingresado no es valido, Ingrese un numero")

validar_signo_numero()