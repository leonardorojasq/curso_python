###############   DIFERENCIA ENTRE ENUMERATE Y DICCIONARIO

# LISTAS
alumnos = ["juan","jose","maria","juana"]

for clave, alumno in enumerate(alumnos, start=1):
    print(clave, alumno)
    
    
    
# DICCIONARIO
alumno = {
    "nombre": "juan",
    "curso": 1001,
    "jornada": "mañana"
}
# usuando Itens()
for clave, valor in alumno.items():
    print(clave, " = ", valor)
    
