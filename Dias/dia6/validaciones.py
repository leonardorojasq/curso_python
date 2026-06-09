import re

def validar_numeros(dato):
    if not dato:
        raise ValueError("No hay ningun numero ,Ingrese uno")
    
    if not dato.isdigit():
        print("Es str")
        
    return int(dato)
    

def actualiza_email(mail):
        regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        
        if not re.match(regex, mail):
            raise ValueError("No coincide")
        
        return mail
    
