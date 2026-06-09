# ejercicio 1
class Usuario:
    # ejercicio 2
    def __init__(self, id , nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email
        
    # Ejercicio 3 crear metodo saludar
    def saludar(self):
        saludar = self.nombre
        
        print("buenos días bienvenido sr", saludar)
        

# 4 Crear objeto
usuario1 = Usuario(4, "Leonardo Rojas Q.", "leonardorojasq@outlook.com")

usuario1.saludar()


#5 Crear lista de objetos
usuarios = [
    
        Usuario(1,"Ana","ana@gmail.com"),
        
        Usuario(2,"Sofia","sofia@gmail.com"),
        
        Usuario(3,"Ester","ester@gmail.com")
        
]

# Recorrer lista e imprimir nombres.
for usuario in usuarios:
    print(
        usuario.id,
          usuario.nombre,
          usuario.email
          )
    
# 7 Buscar usuario por id.
for usuario in usuarios:
    
    if usuario.id == 2:
        print("Usuario encontrado es:", usuario.nombre)
        break
    
else:
    print("Usuario no existente")
    

# 8 actualizar el email
for usuario in usuarios:
    
    if usuario.id == 2:
        usuario.email = "gerencia@gmail.com"
        break
    
else:
    print("Usuario no existente")
    

# 9 eliminar un objeto
for usuario in usuarios:
    
    if usuario.id == 2:
        usuarios.remove(usuario)
        break
else:
    print("El objeto no existe")


# verificar que el obk¿jwto 2 halla sido eliminado
for usuario in usuarios:
    print(
        usuario.id,
          usuario.nombre,
          usuario.email
          )
    