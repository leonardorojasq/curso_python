p = 's'
suma = 0

while p == 's':

    m = int(input("Ingrese el valor: "))
    suma += m

    p = input("Desea seguir? S o N: ").lower()

print("La suma total es:", suma)