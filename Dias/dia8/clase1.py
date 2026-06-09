import re

#======================================================
# Validaciones
#======================================================
def validar_texto(texto):
    if not isinstance(texto, str):
        raise ValueError("No se admiten numero so caracteres especiales")
    
    if not texto.strip():
        raise ValueError("No puuede venir vacio")

    if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ ]+$', texto):
        raise ValueError("Solo letras")
        
    return texto

def validar_email(email):
    regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    
    if not re.match(regex, email):
      
      raise ValueError("Email inválido")

    return email  

def verificar_numero_positivo(numero):

    if not isinstance(numero, int):
        raise ValueError("Debe ser un número entero")

    if numero < 0:
        raise ValueError("El número debe ser positivo")

    return numero



#======================================================
# Clase Usuario
#======================================================

class Usuario:
    
    def __init__(self, id, nombre, email):
        self.id = verificar_numero_positivo(id)
        self.nombre = validar_texto(nombre)
        self.email = validar_email(email)
        
    def __str__(self):
        return f'{self.id} {self.nombre} {self.email}'
    
   
    
    #======================================================
    # Metodos
    #======================================================
    
    def actualizar_nombre(self, nuevo_nombre):
        validar_texto(nuevo_nombre)
        self.nombre = nuevo_nombre
            
        return self
    
    def actualizar_email(self, email):
        validar_email(email)
        self.email = email
        
        return self
    
    def mostrar_informacion(self):
        
        return f'ID: {self.id}\nNombre: {self.nombre}\nEmail: {self.email}'
                

#======================================================
# Lista de Usuarios
#======================================================

usuarios = []


leonardo = Usuario(3,"ana","ana@gamil.com")

print(leonardo.mostrar_informacion())
