num1 = int(input("Ingresa el primer numero"))
num2 = int(input("Ingresa el siguiente numero"))

def suma(data1, data2):
    result = data1+data2
    return f'La suma de {data1} + {data2} es: {result}'


def resta(data1,data2):
    result = data1 - data2
    return f'la resta de {data1} - {data2} es: {result}'


def mul(data1,data2):
    result = data1*data2
    return f'La multiplicación entre {data1} x {data2} es: {result}'

def divi(data1,data2):
    result = data1 / data2
    return f'La división entre {data1} / {data2} es: {result}'


print(suma(num1,num2))
print(resta(num1,num2))
print(mul(num1,num2))