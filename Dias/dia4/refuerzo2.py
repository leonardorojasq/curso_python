usuarios = [

    {"id":1, "nombre":"Leo"},

    {"id":2, "nombre":"Ana"},
    
    {"id":3, "nombre":"Rodolfo"},
]

buscar_id  = 2

# bandera flag
encontrado = False

for usuario in usuarios:

    if usuario["id"] == buscar_id:
        print("Encontrado")
        break

else:
    print("No existe")