#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Nombre:       Sem7Des2_AlejandroDruetta.py
# Fecha:        05/06/13
# Autor:        Alejandro Druetta

""" Administrar una lista de inscriptos a un curso.

    El programa nos permite ingresar los datos del alumno, realizar
    búsquedas, informes, corregir datos y eliminar registros. """

from textwrap import dedent
import os

campos = ("Nombre", "Edad", "Teléfono", "E-mail", "Localidad")

def menu_principal(diccionario):

    registro = 0

    while True:

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
            opcion = input("Digite una opción (1-6): ")

        while opcion not in "123456":
            opcion = input(dedent("\nError: Opción inexistente.\n"
                                  "Por favor, ingrese una opción válida del "
                                  "menú: "))

        if opcion == "1":
            diccionario, registro = agregar(diccionario, registro)
        elif opcion == "2":
            registro = buscar(diccionario)
            input("\n")
        elif opcion == "3":
            diccionario = corregir(diccionario)
        elif opcion == "4":
            diccionario = eliminar(diccionario)
        elif opcion == "5":
            listar(diccionario)
        else:
            print("\nFinalizado.\n")
            break

def agregar(diccionario, registro):
    """ Agrega los datos del alumno al diccionario. Recibe el diccionario y
        el código del alumno y devuelve los mismos datos actualizados. """

    while True:
        registro += 1

        print("\n*** Ingrese los campos del alumno registro N° %d ***\n"
              % registro)

        apellido = input("    Apellido: \t")
        nombre = input("    Nombre: \t")
        edad = input("    Edad: \t")
        telefono = input("    Teléfono: \t")
        email = input("    E-mail: \t")
        localidad = input("    Localidad: \t")

        diccionario[str(registro)] = [apellido + ", " + nombre, edad, telefono,
                                      email, localidad]

        opcion = input("\n¿Ingresa más alumnos (S/N)?: ").lower()
        if opcion != "s":
            break

    return diccionario, registro

def buscar(diccionario):
    """ Busca los datos de un alumno según el código de inscripción.
        Recibe el diccionario y una tupla con los nombres de los campos
        y devuelve el número de código. """

    registro = input("\nIngrese el código del alumno ('0' para salir): ")

    # Si no está en el diccionario da error.
    while registro not in diccionario:
        registro = input(dedent("""\nError: El código todavía no existe.
                                Ingrese nuevamente: """))

    # Muestra los datos del alumno.
    visualizar(diccionario, registro)

    return registro

def visualizar(diccionario, registro):
    """ Muestra los datos de un alumno. Recibe el diccionario, el código del
        alumno y el nombre de los campos. Imprime en pantalla. """

    print("\n*** Datos del alumno registro N° %s ***\n" % registro)

    for i in range(5):
        print("%d. %s: \t%s" % (i+1, campos[i], diccionario[registro][i]))

def corregir(diccionario):

    registro = buscar(diccionario)
    campo = int(input("\n¿Qué campo desea modificar (1-6) '0' para Guardar: "))

    while campo not in range(7):
        campo = int(input("Error: Opción inválida. \nIngrese nuevamente: "))

    if campo in range(1, 7):
        diccionario[registro][campo-1] = input("\n%s: " % campos[campo-1])

    visualizar(diccionario, registro)

    print("\nCorregido el campo '%s' del registro N° %s." % (campos[campo-1],
          registro))
    input("\n")
    return diccionario

def eliminar(diccionario):
    """ Elimina el registro de un alumno según la búsqueda que hace por el
        código de inscripción. Devuelve el diccionario actualizado. """

    registro = buscar(diccionario)
    confirma = input("\n¿Está seguro (S/N)?: ").lower()

    if confirma == "s":
        diccionario.pop(registro)
        input("\nEliminado el registro N° %s." % registro)
    else:
        input("\nEl registro del alumno no será eliminado.")

    return diccionario

def listar(diccionario):
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
