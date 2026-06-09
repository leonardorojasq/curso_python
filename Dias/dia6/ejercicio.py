from validaciones import validar_numeros, actualiza_email


# =========================
# CLASE
# =========================

class Usuario:

    def __init__(self, id, nombre, email):

        self.id = id
        self.nombre = nombre
        self.email = email


    def __str__(self):

        return f'Usuario: {self.nombre} - {self.email}'


    # MÉTODO
    # MODIFICA EL OBJETO ACTUAL
    def actualizar_email(self, nuevo_email):

        self.email = nuevo_email


    # MÉTODO
    # MUESTRA EL OBJETO ACTUAL
    def mostrar_usuario(self):

        return f'{self.id} {self.nombre} {self.email}'


# =========================
# FUNCIÓN EXTERNA
# NO PERTENECE A USUARIO
# =========================

def es_mayor_edad(edad):

    if edad >= 18:
        return "Es mayor de edad"

    return "No es mayor de edad"


# =========================
# LISTA DE OBJETOS
# =========================

usuarios = [

    Usuario(2, "Ana", "ana@gmail.com")

]


# =========================
# FUNCIONES DEL SISTEMA
# =========================

def cambiar_correo():

    id = validar_numeros(
        input("Ingrese el id: ")
    )

    for usuario in usuarios:

        if usuario.id == id:

            nuevo_email = actualiza_email(
                input("Nuevo email: ")
            )

            usuario.actualizar_email(
                nuevo_email
            )

            print("Email actualizado")

            break

    else:
        print("Usuario no encontrado")


def mostrar_todos_los_usuarios():

    for usuario in usuarios:

        print(usuario)


def validar_edad():

    edad = validar_numeros(
        input("Ingrese edad: ")
    )

    return es_mayor_edad(edad)


# =========================
# OBJETOS
# =========================

usuario1 = Usuario(
    1,
    "Ester",
    "ester@gmail.com"
)

usuarios.append(usuario1)


# =========================
# PRUEBAS
# =========================

print(usuario1.mostrar_usuario())


# REFERENCIA
au = usuario1

au.email = "oscar@dondees.com"

print(au)


# VALIDAR MAYORÍA EDAD
print(validar_edad())


# MOSTRAR CAMBIO
print(usuario1.mostrar_usuario())


# MOSTRAR TODOS
mostrar_todos_los_usuarios()


# CAMBIAR CORREO
# cambiar_correo()