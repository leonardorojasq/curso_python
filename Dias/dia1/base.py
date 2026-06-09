base = float(input("Ingresa la Base: "))
altura = float(input("Ingresa la Altura: "))




def calcula(data1, data2):
    result = (data1 * data2)/2
    return f'La baase {data1} x la Altura {data2} es: {result}'


print(calcula(base,altura))