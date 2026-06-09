#RETO IMPORTANTE
#
#Haz un sistema menú que:
#
#1. Sumar
#2. Restar
#3. Multiplicar
#4. Dividir
#5. Salir
#Y:
#siga funcionando hasta salir,
#valide opciones incorrectas.


def suma(num1,num2):
    r = num1 + num2
    print(f'La suma de {num1} + {num2} es numeros es: {r}')
    
def resta(num1,num2):
    r = num1 - num2
    print(f'La suma de {num1} - {num2} es numeros es: {r}')

def division(num1,num2):
    if num2 == 0:
        print("No se puede dividir por cero")
    else:
        r = num1 / num2
        print(f'La suma de {num1} / {num2} es numeros es: {r}')

def multiplicacion(num1,num2):
    r = num1 * num2
    print(f'La suma de {num1} X {num2} es numeros es: {r}')

def calculadora_pro():
    
    while  True:
    
        print("Elija la operación a realizar")
        print("1. Sumar")
        print("2. Restar")
        print("3. Dividir")
        print("4. Multiplicar")
        print("5. Salir")
        
        resultado = input("Elige una opcion ")
        
        #validar opcion
        if not resultado.isdigit():
            print("Debes ingresar un numero")
            continue
        
        resultado = int(resultado)
        
        #OPCION SALIR
        if resultado == 5:
            print("Saliendo...")
            break
        
        #validar que el numero este en el rango
        if resultado < 0 or resultado > 5:
            print("No estas en el rango  de opciones")
            continue
        
        
               
        print("Ahora ingresa los numeros para realizar la operación\n")
        num1 = input("Ingresa el primer numero: ")
        num2 = input("Ingresa el seundo numero: ")
                    
        if num1.isdigit() and num2.isdigit() :
                num1 = float(num1)
                num2 = float(num2)
  

                if resultado == 1:
                    suma(num1,num2)
                elif resultado == 2:
                    resta(num1,num2)
                elif resultado == 3:
                    division(num1,num2)
                elif resultado == 4:
                   multiplicacion(num1,num2)
    
        else:
            print("Solo se aceptan numeros")
        
    
    

calculadora_pro()
