#EJERCICIO 3
#
#Pide una nota de 0 a 5.
#
#Mostrar:
#
#Excelente.
#Aprobado.
#Reprobado.

def pedir_nota():
    nota = input("Ingresa la Nota de 0 a 5: ")
    
    if nota.isdigit():
        nota = int(nota)
        
        
        if nota < 3:
            print("Reprobado")
        elif nota == 3:
            print("Aprobado")
        elif nota > 3 and nota <= 5:
            print("Excelente")
        else: 
            print("La nta debeser entre 0 y 5")
    else:
        print("El caracter ingresado no es valido, Ingresa un numero entre 0 y 5")
        
        
        
pedir_nota()