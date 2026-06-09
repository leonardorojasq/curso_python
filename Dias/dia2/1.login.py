# MINI PROYECTO — LOGIN
#OBJETIVO
#Crear un mini login.
#
#REGLAS
#Usuario correcto:
#admin
#
#Password correcta:
#1234
#SI TODO ESTÁ BIEN
#
#Mostrar:
#Bienvenido administrador
#Credenciales incorrectas
def validar_credenciales(username,password):
        
    if username == 'admin' and password=='1234':
        print("Bienvenido administrador")
    else:
        print("Credenciales incorrectas")
    

def login():
    username = input("Ingrese el Usuario: ")
    password = input("Ingrese el Passwsord")
    
    validar_credenciales(username,password)
    

login()
        
