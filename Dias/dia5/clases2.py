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

    Usuario(1, "Leon", 35, "leo@gmail.com"),

    Usuario(2, "Ana", 25, "ana@gmail.com")
]


usuario1 = Usuario(1, "leonardo","34","fkfkf")

usuario1.saludar()

usuario2 = usuario1

print(usuario2.nombre)