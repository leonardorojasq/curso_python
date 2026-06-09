usuarios = [

    {"id":1, "nombre":"Leo"},

    {"id":2, "nombre":"Ana"},
    
    {"id":3, "nombre":"Rodolfo"},
]



# actualizar
for usuario in usuarios:
    
    if usuario["id"] == 2:
        
        usuario["nombre"] = "Ester"
        
        print(usuario["nombre"])
        