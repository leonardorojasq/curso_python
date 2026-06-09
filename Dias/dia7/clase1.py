import re
# 1. CRUD REAL ORGANIZADO
# crear
# listar
# buscar
# actualizar
# eliminar

class Usuario:
    
    def __init__(self, id, nombre, email):
        self.id = id
        self.nombre = nombre
        self.email = email

    def __str__(self):
        return f'{self.nombre} {self.email}'

        

# lista de usuario
usuarios = [
    Usuario(1, "Antonela", "antonela@gmail.com"),
    Usuario(2, "Leonardo", "leonardorojasq@gmail.com")
]


# =========================
# VALIDACIONES
# =========================
def verificar_numero_positivo(numero):

    if not isinstance(numero, int):
        raise ValueError("Debe ser un número entero")

    if numero < 0:
        raise ValueError("El número debe ser positivo")

    return numero



def validar_email(email):
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if not re.match(regex, email):
      
      raise ValueError("Email inválido")

    return email  
    

def validar_texto(texto):
    
    if not texto.strip():
        raise ValueError("El campo está vacío")
    
    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$', texto):
        raise ValueError("Solo letras")
    
    return texto
        

    
#==========================
# FUNCIONES
#==========================
# 1 uscar por id
def buscar_usuario_por_id(id):
    try:
        id = verificar_numero_positivo(id)
        
        for usuario in usuarios:
            if usuario.id == id:
                return usuario
        return None
    except ValueError as e:
        print(f'Error {e}')
    
# 2 actualizar nombre"
def actualizar_usuario_por_id(id, nuevo_nombre):
    try:
        id = verificar_numero_positivo(id)

        actualizar_nombre = buscar_usuario_por_id(id)
        
        if actualizar_nombre:
            actualizar_nombre.nombre = nuevo_nombre
            
            return actualizar_nombre
        
        return None
    except ValueError as e:
        print(f'Error {e}')  

def eliminar_usuario_por_id(id):
    try:
        usuario = buscar_usuario_por_id(id)
        
        if usuario:
            usuarios.remove(usuario)
            
            return "Usuario eliminado con exito"
        
        return None
    except ValueError as e:
        print(f'Error {e}')


# EJERCICIO 4 — CREAR USUARIO VALIDANDO IDS DUPLICADOS
def crear_usuario(id, nombre, email):
    try:
        id = verificar_numero_positivo(id)
        
        nombre = validar_texto(nombre)
        
        email = validar_email(email)
        
        if buscar_usuario_por_id(id):
            raise ValueError("Verifica el ID ya existe o estas enviando un str")
        
        else:
            usuario = Usuario(id,nombre, email)
            usuarios.append(usuario)
            
        return "Usuario creado con exito"        
    except ValueError as e:
        print(f'Error {e}')

def listar_todos_los_usuarios():
        return usuarios



print("\n## LISTAR USUARIOS ##")
for usuario in listar_todos_los_usuarios():
    print(usuario)

crear_usuario(4, "Andrea", "andrea@outlook.com")
print("\n## LISTAR USUARIOS ##")               
for usuario in listar_todos_los_usuarios():
    print(usuario)

print("\n## BUSCAR USUARIO POR ID ##")
print(buscar_usuario_por_id(1))

print("\n## ACTUALIZAR NOMBRE USUARIO##")
print(actualizar_usuario_por_id(2,"Teddy"))

print(eliminar_usuario_por_id(2))

print("\n## LISTAR USUARIOS ##")
for usuario in listar_todos_los_usuarios():
    print(usuario)