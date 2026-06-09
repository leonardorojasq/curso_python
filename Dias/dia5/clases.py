class Usuario:
    
    def __init__(self, id, nombre, edad, email):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.email = email
    
    def saludar(self):
        saludo = self.nombre
        print("Hola ", saludo)


usuarios = [

    Usuario(1, "Leo", 35, "leo@gmail.com"),

    Usuario(2, "Ana", 25, "ana@gmail.com")
]


usuario1 = Usuario(1, "leo","34","fkfkf")

usuario1.saludar()

#Crear
nuevo = Usuario(3,"Ester" , 28, "ester@gmail.com")
usuarios.append(nuevo)

# listar
for usuario in usuarios:

    print(usuario.id, usuario.nombre, usuario.edad, usuario.email)
    

# buscar
for usuario in usuarios:
    
    if usuario.id == 2:
        print(usuario.nombre)
        break
    
else:
    print("No se encontro coincidencia")
    
    
# actualizar
for usuario in usuarios:
    
    if usuario.id == 3:
        print(usuario.nombre)
        usuario.nombre = "Mardoqueo"
        print(usuario.nombre)
        break
    
else:
    print("No se encontro coincidencia")
    
    
# eliminar
for usuario in usuarios:
    
    if usuario.id == 3:
        usuarios.remove(usuario)
        break
    
else:
    print("No se encontro coincidencia")
    
    
    
for usuario in usuarios:
    print(usuario.id, usuario.nombre, usuario.edad, usuario.email)