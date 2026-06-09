#EJERCICIO 1
#
#Usar:
#
#try
#except ValueError
#
#para validar enteros.


def validar_enteros():
    try: 
        num = int(input("Ingrese el numero: "))
        print("Es entero",num)
    except ValueError as e:
        print("Error: El valor es un decimal",e)
            

validar_enteros()