import re

# =========================
# CLASE
# =========================

class Usuario:

    def __init__(self, id, nombre, edad, email):

        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.email = email


# =========================
# BASE DE DATOS TEMPORAL
# =========================

usuarios = []


# =========================
# VALIDACIONES
# =========================

def validar_numero(dato):

    if not dato.isdigit():
        raise ValueError("Debes ingresar números")

    numero = int(dato)

    if numero <= 0:
        raise ValueError("El número debe ser positivo")

    return numero


def validar_texto(texto):

    if not texto.strip():
        raise ValueError("El campo está vacío")

    if texto.isdigit():
        raise ValueError("No debes ingresar números")

    return texto


def validar_email(email):

    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'

    if not re.match(patron, email):
        raise ValueError("Email inválido")

    return email


# =========================
# CREAR
# =========================

def crear():

    try:

        id = validar_numero(
            input("Agregar id: ")
        )

        # VALIDAR ID REPETIDO
        for usuario in usuarios:

            if usuario.id == id:
                raise ValueError(
                    "El id ya existe"
                )

        nombre = validar_texto(
            input("Agregar nombre: ")
        )

        edad = validar_numero(
            input("Agregar edad: ")
        )

        email = validar_email(
            input("Agregar email: ")
        )

        usuario = Usuario(
            id,
            nombre,
            edad,
            email
        )

        usuarios.append(usuario)

        print("Usuario creado correctamente")

    except ValueError as e:
        print("Error:", e)


# =========================
# LISTAR
# =========================

def listar():

    if not usuarios:
        print("No hay usuarios")
        return

    print("\nLISTADO DE USUARIOS\n")

    for usuario in usuarios:

        print(
            f"""
ID: {usuario.id}
Nombre: {usuario.nombre}
Edad: {usuario.edad}
Email: {usuario.email}
"""
        )


# =========================
# BUSCAR
# =========================

def buscar():

    try:

        id_buscar = validar_numero(
            input("Ingrese el id: ")
        )

        for usuario in usuarios:

            if usuario.id == id_buscar:

                print(
                    f"""
Usuario encontrado

Nombre: {usuario.nombre}
Edad: {usuario.edad}
Email: {usuario.email}
"""
                )

                break

        else:
            print("Usuario no encontrado")

    except ValueError as e:
        print("Error:", e)


# =========================
# ACTUALIZAR
# =========================

def actualizar():

    try:

        id_buscar = validar_numero(
            input("Ingrese el id del usuario: ")
        )

        for usuario in usuarios:

            if usuario.id == id_buscar:

                nuevo_nombre = validar_texto(
                    input("Nuevo nombre: ")
                )

                usuario.nombre = nuevo_nombre

                print("Usuario actualizado")

                break

        else:
            print("Usuario no encontrado")

    except ValueError as e:
        print("Error:", e)


# =========================
# ELIMINAR
# =========================

def eliminar():

    try:

        id_buscar = validar_numero(
            input("Ingrese el id a eliminar: ")
        )

        for usuario in usuarios:

            if usuario.id == id_buscar:

                usuarios.remove(usuario)

                print("Usuario eliminado")

                break

        else:
            print("Usuario no encontrado")

    except ValueError as e:
        print("Error:", e)


# =========================
# MENU
# =========================

def menu():

    while True:

        print("""
======== MENU ========

1. Crear usuario
2. Listar usuarios
3. Buscar usuario
4. Actualizar usuario
5. Eliminar usuario
6. Salir

======================
""")

        try:

            opcion = validar_numero(
                input("Ingrese opción: ")
            )

            if opcion < 1 or opcion > 6:
                raise ValueError(
                    "Opción inválida"
                )

            if opcion == 1:
                crear()

            elif opcion == 2:
                listar()

            elif opcion == 3:
                buscar()

            elif opcion == 4:
                actualizar()

            elif opcion == 5:
                eliminar()

            elif opcion == 6:
                print("Saliendo...")
                break

        except ValueError as e:
            print("Error:", e)


menu()