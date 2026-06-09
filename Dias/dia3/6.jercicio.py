# try:
#     edad = -5

#     if edad < 0:
#         raise ValueError("No es un numero valido ")
# except ValueError as e:
#     print(f'Error, el caracter no es valido: {edad}', e )
    
    
    
    
# edad = "20"

# if not isinstance(edad, int):
#     raise TypeError(
#         "La edad debe ser un número entero"
#     )

# print("Edad válida")



# numero = "20"

# print(
#     isinstance(numero, int)
# )

# print("El programa sigue")






# def login():

#     try:

#         edad = "LEo"

#         if edad ==6:

#             raise ValueError("Edad inválida")
#         else: print("Error")



#     except ValueError as e:

#         print(e)

#         return "Error controlado", 400
# login()


lista = [1,2,3]
lista.append(4)
lista.extend([5,6,7,8,9,10])
print(lista)
lista.pop()
print(f'Eliminado {lista}')
lista.remove(4)
print(lista)
del lista[1]
print(lista)

for clave, valor in enumerate(lista, start=0):
    print(clave,valor)