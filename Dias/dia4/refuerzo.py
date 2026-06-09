usuarios = {
    "nombre": "leo",
    "edad": 26
}


print(len(usuarios))

# imprime claves
for usuario in usuarios:
    print(usuario)

# imprime clave y valor , Convierte el diccionario en pares:
for clave, valor in usuarios.items():
    print(clave, valor)

# Porque recorrer un diccionario DIRECTAMENTE por claves:
for clave, valor in enumerate(usuarios):
    print(clave, valor)
    
    
    
for x in usuarios.keys():
    print("Clave ", x)
    
for i in range(len(usuarios)):
    print(" Esto es len", i)