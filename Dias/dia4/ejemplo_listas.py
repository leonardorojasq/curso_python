usuarios = [
    {"id": 1, "nombre": "Leo"},
    {"id": 2, "nombre": "Ana"},
]

for indice, usuario in enumerate(usuarios):
    if usuario=="Leo":
        usuario.pop(indice)

print(indice, usuario)
    
    
 