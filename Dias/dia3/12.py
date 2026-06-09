# EJERCICIO 6

# Lanzar error con raise.



try:
    edad = input("Ingrese una edad mayor a 18: ")
    
    
    if  edad.isdigit():
        edad = int(edad)
        
    if edad >18:
        print("Acceso premitido")
    else:
        raise ValueError("Acceso denegado no calificas... ")
    
        
except Exception as e:
    print(e)