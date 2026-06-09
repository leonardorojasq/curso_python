# EJERCICIO 5

# Usar:

# múltiples except.


try:
    
    num = input("ingrese el número: ")
    
    if num.isdigit():
        print("No ingreses letras solo numeros")
    
    
    num = int(num)
        
    n = num * 5
    
    result = 10 / n
    
    print(result)
    
except ZeroDivisionError as e:
    print("No puedes dividir por cero")
except TypeError as e:
    print("El valor no es el esperado, no string o decimales")
except ValueError as e:
    print("No puedes dividir 10 conun string")
except FloatingPointError as e:
    print("Error matemático de punto flotante")
except Exception:
    print("Este error es mas complejo")
finally:
    print("Saliendo del programa")