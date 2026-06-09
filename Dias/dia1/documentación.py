DÍA 1 — FUNDAMENTOS PYTHON

Hoy vas a aprender:

Variables.
Tipos de datos.
input().
print().
Conversión de tipos.
Operaciones matemáticas.
Primer mini proyecto.

Objetivo:
Que entiendas cómo piensa Python.


1. VARIABLES

Una variable guarda información.

Ejemplo:

nombre = "Leonardo"
edad = 25
altura = 1.75

Aquí:

nombre guarda texto.
edad guarda enteros.
altura guarda decimales.
2. TIPOS DE DATOS
Texto → string
nombre = "Carlos"
Entero → int
edad = 20
Decimal → float
precio = 19.99
Booleano → bool
activo = True
3. PRINT()

Sirve para mostrar información.

print("Hola mundo")
nombre = "Leonardo"

print(nombre)
4. INPUT()

Sirve para pedir datos al usuario.

nombre = input("Ingresa tu nombre: ")

print(nombre)
IMPORTANTE

input() SIEMPRE devuelve texto.

Por eso:

edad = input("Edad: ")

Aunque escribas 20, Python lo guarda como string.

5. CONVERSIÓN DE DATOS
String → int
edad = int(input("Edad: "))
String → float
precio = float(input("Precio: "))
6. OPERACIONES MATEMÁTICAS
Suma
a = 10
b = 5

print(a + b)
Resta
print(a - b)
Multiplicación
print(a * b)
División
print(a / b)
7. CONCATENAR TEXTO
nombre = "Leonardo"

print("Hola " + nombre)
8. F-STRINGS (MUY IMPORTANTE)

Forma profesional.

nombre = "Leonardo"
edad = 25

print(f"Hola {nombre}, tienes {edad} años")

Apréndelo desde ya.

PRIMER PROGRAMA
nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))

print(f"Hola {nombre}")
print(f"Tienes {edad} años")