# LISTAS
usuarios = [
    {"id":1, "nombre":"Leo"},
    {"id":2, "nombre":"Ana"},
]


usuarios.append({"id":3, "nombre": "Carlos"})
for usuario in usuarios:
    print(usuario["nombre"])
    
    
for usuario in usuarios:
    if usuario["id"] == 2:
        usuario["nombre"] = "Sofia"
        print(usuario["nombre"])


for usuario in usuarios:
    if usuario["nombre"] == "Leo":
        usuarios.remove(usuario)
        break
print(usuarios)


