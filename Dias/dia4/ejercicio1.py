# "EJERCICIO 1

# Crear diccionario:
# nombre
# edad
# ciudad

# Mostrar datos."


usuarios = {
    "nombre": "Juan",
    "ciudad": "monteria",
    "edad": 36
    }

#Actualizar datos
usuarios[0]["nombre"] = "Leonardo"

#Agregar
usuarios[0]["email"] = "leonardorojasqrlp.com.co"

#Usar Get
telefono = usuarios.get("telefono", "No existe")

# Recorrer .items().
for clave, valor in usuarios.items():
    print(clave, valor)
    
 # Buscar usuario por ID.   
for indice in usuarios:
    if indice == 1:
        print(indice)
        
# Actualizar email.
usuarios[0]["email"] = "leonardorojasq@outlook.com"


buscar_id = 2

for usuario in usuarios:

    if usuario["id"] == buscar_id:
        print(usuario)