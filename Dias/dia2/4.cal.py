#EJERCICIO 5
#
#Pide dos números y una operación:
#
#+
#-
#*
#/
#
#Y ejecutar operación usando if.
def suma(num1,num2):
    r = num1 + num2
    print(f'La suma de {num1} + {num2} es numeros es: {r}')
    
def resta(num1,num2):
    r = num1 - num2
    print(f'La suma de {num1} - {num2} es numeros es: {r}')

def division(num1,num2):
    r = num1 / num2
    print(f'La suma de {num1} / {num2} es numeros es: {r}')

def multiplicacion(num1,num2):
    r = num1 * num2
    print(f'La suma de {num1} X {num2} es numeros es: {r}')
    
def calculadora():
    print("Calculadora Moderna 1.0")
    
    num1 = input("Ingresa el primer numero: ")
    num2 = input("Ingresa el seundo numero: ")
    print("Elija la operación a realizar")
    print("1. Sumar")
    print("2. Restar")
    print("3. Dividir")
    print("4. Multiplicar")
    resultado = input("Elige una opcion ")
    
    if num1.isdigit() and num2.isdigit() and resultado.isdigit():
        num1 = int(num1)
        num2 = int(num2)
        resultado = float(resultado)
        
        if resultado == 1:
            suma(num1,num2)
        elif resultado == 2:
            resta(num1,num2)
        elif resultado == 3:
            division(num1,num2)
        elif resultado == 4:
           multiplicacion(num1,num2)
        else:
            print("Este caracter no es valido")
        
    
    else:
        print("Solo se aceptan numeros")
        
        
calculadora()