#! /usr/bin/env python3

def menu_principal(diccionario):

    registro = 0
    campos = ("Nombre", "Edad", "Teléfono", "E-mail", "Localidad")

    while True:

        import os
        os.system('clear')  # Limpia la pantalla.

        if diccionario == {}:
            opcion = "1"
        else:
            print("""\n*** Menú Principal ***

    1. Agregar
    2. Buscar
    3. Corregir
    4. Eliminar
    5. Listados
    6. Salir
    """)
            opcion = str(input("Digite una opción (1-6): "))

        while opcion not in "123456":
            opcion = str(input("\nError: Opción inexistente. \nPor favor, \
ingrese una opción válida del menú: "))

        if opcion == "1":
            diccionario, registro = agregar(diccionario, registro)
        elif opcion == "2":
            registro = buscar(diccionario, campos)
            input("\n")
        elif opcion == "3":
            diccionario = corregir(diccionario, campos)
        elif opcion == "4":
            diccionario = eliminar(diccionario, campos)
        elif opcion == "5":
            listar(diccionario, campos)
        else:
            print("\nFinalizado.\n")
            break


def agregar(diccionario, registro):
    """ Agrega los datos del alumno al diccionario. Recibe el diccionario y
        el código del alumno y devuelve los mismos datos actualizados. """

    while True:
        registro += 1

        print("\n*** Ingrese los campos del alumno registro N° %d ***\n" \
              % registro)

        apellido = str(input("    Apellido: \t"))
        nombre = str(input("    Nombre: \t"))
        edad = str(input("    Edad: \t"))
        telefono = str(input("    Teléfono: \t"))
        email = str(input("    E-mail: \t"))
        localidad = str(input("    Localidad: \t"))

        diccionario[str(registro)] = [apellido + ", " + nombre, edad, telefono,
                                      email, localidad]

        opcion = str(input("\n¿Ingresa más alumnos (S/N)?: ")).lower()
        if opcion != "s":
            break

    return diccionario, registro


def buscar(diccionario, campos):
    """ Busca los datos de un alumno según el código de inscripción.
        Recibe el diccionario y una tupla con los nombres de los campos
        y devuelve el número de código. """

    registro = str(input("\nIngrese el código del alumno ('0' para salir): "))

    # Si no está en el diccionario da error.
    while registro not in diccionario:
        registro = str(input("\nError: El código todavía no existe. \nIngrese \
nuevamente: "))

    # Muestra los datos del alumno.
    visualizar(diccionario, registro, campos)

    return registro


def visualizar(diccionario, registro, campos):
    """ Muestra los datos de un alumno. Recibe el diccionario, el código del
        alumno y el nombre de los campos. Imprime en pantalla. """

    print("\n*** Datos del alumno registro N° %s ***\n" % registro)

    for i in range(5):
        print("%d. %s: \t%s" % (i+1, campos[i], diccionario[registro][i]))


def corregir(diccionario, campos):

    registro = buscar(diccionario, campos)
    campo = int(input("\n¿Qué campo desea modificar (1-6) '0' para Guardar: "))

    while campo not in range(7):
        campo = int(input("Error: Opción inválida. \nIngrese nuevamente: "))

    if campo in range(1, 7):
        diccionario[registro][campo-1] = input("\n%s: " % campos[campo-1])
    visualizar(diccionario, registro, campos)

    print("\nCorregido el campo '%s' del registro N° %s." % (campos[campo-1], \
          registro))
    input("\n")
    return diccionario


def eliminar(diccionario, campos):
    """ Elimina el registro de un alumno según la búsqueda que hace por el
        código de inscripción. Devuelve el diccionario actualizado. """

    registro = buscar(diccionario, campos)
    confirma = str(input("\n¿Está seguro (S/N)?: ")).lower()

    if confirma == "s":
        diccionario.pop(registro)
        input("\nEliminado el registro N° %s." % registro)
    else:
        input("\nEl registro del alumno no será eliminado.")

    return diccionario


def listar(diccionario, campos):
    """ Imprime un listado en pantalla del registro de inscriptos al curso. """

    campos_len = (23, 5, 12, 23, 12)
    posicion = 0

    print("Cod. ", end="")
    for i in campos:
        print(i, end=" " * (campos_len[posicion] - len(i)))
        posicion += 1

    print("-" * 80)
    for entrada in diccionario:
        print(entrada.rjust(4), end=" ")
        posicion = 0
        for campo in diccionario[entrada]:
            print(campo, end=" " * (campos_len[posicion] - len(campo)))
            posicion += 1

    input()


def main():

    diccionario = {}
    menu_principal(diccionario)

main()
