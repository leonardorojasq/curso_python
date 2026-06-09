num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el siguiente numero: "))

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

print## ¿Que acción deseas realizar?()
print("1. Sumar")
print("2. Restar")
print("3. multiplicar")
print("4. Dividir")
accion = int(input("Opcion: "))
if accion == 1:
    print(suma(num1,num2))
elif accion==2:
    print(resta(num1,num2))
elif accion == 3:
    print(mul(num1,num2))
elif accion==4:
    print(divi(num1,num2))







