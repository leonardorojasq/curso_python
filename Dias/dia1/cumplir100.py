nombre = str(input("Ingresa tu nombre "))
edad = int(input("Ingresa tu edad "))

def clacular(data1, data2):
    tiempo = 100
    result = tiempo - data2

    return f'Hola {data1} tu tienes {data2} y te faltan {result} para cumplir 100 años.'


print(clacular(nombre, edad))