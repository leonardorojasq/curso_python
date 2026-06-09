precio = float(input("Ingresa el precio del producto: $ "))
cantidad = int(input("Ingrese la cantidad: "))


def calcular(data1, data2):
    return  f'El  total es: {data1 * data2}'


print(calcular(precio, cantidad))