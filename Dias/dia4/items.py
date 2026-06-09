frase = "leonardo rojas quevedo"

vocales = "aeiouAEIOUÁÉÍÓÚ"
contador = 0

for f in frase:
    if f in vocales:
        contador+=1

print(contador)

usuario = {
    "nombre": "leonardo rojas",
    "cargo": "Jefe",
    "edad": 50
    }

usuario["ciudad"] = "Bogotá"
usuario["dirección"] = "cra 52a 134a 56"
usuario["dirección"] = "cra 52a 134a 56 apto 105"
del usuario["edad"]
usuario.get("telefono", "No existe")
print(usuario.keys())
print(usuario.values())


for clave, valor in usuario.items():
    print(clave, valor)
    
    
print(usuario)