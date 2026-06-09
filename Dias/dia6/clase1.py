class Usuario:

    def __init__(self, nombre):

        self.nombre = nombre



    def __str__(self):

        return f"Usuario: {self.nombre}"
    

usuario = Usuario("juan")
print(usuario)

u=usuario.nombre = "leo"
print(u)
print(usuario)