#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# Nombre:       Sem9Des1_AlejandroDruetta.py
# Fecha:        17/06/13
# Autor:        Alejandro Druetta
#
# Propósito:    Agenda Electrónica.


import os


# Funciones de ingreso de datos de contacto.

def ingresar_contacto():
    """ Ingresar los datos de la clave del contacto. """

    apellido = input("      Apellido:".ljust(20)).title()
    nombre = input("      Nombre:".ljust(20)).title()

    return apellido, nombre

def ingresar_datos_contacto():
    """ Ingresar los datos del contacto. """

    telefono = input("      Teléfono:".ljust(20))
    email = input("      E-mail:".ljust(20))
    # Evita que se ingresen datos con comas en la dirección.
    direccion = input("      Dirección:".ljust(20)).replace(",", "")

    return telefono, email, direccion

def contacto_existe(agenda, contacto):
    """ Verifica si el contacto existe. Si existe imprime los datos del
        contacto y devuelve True, sino, devuelve False. """
    
    if contacto in agenda:
        existe = True
        # Imprimir los datos del contacto.
        print("      Teléfono:".ljust(20) + agenda[contacto][0])
        print("      E-mail:".ljust(20) + agenda[contacto][1])
        print("      Dirección:".ljust(20) + agenda[contacto][2])
    else:
        existe = False

    return existe


# Funciones de operación con datos de contacto.

def menu_principal():

    os.system('clear')

    print("""\n\n\n
                        ╔════════════════════════════════╗
                        ║                                ║
                        ║     *** Menú Principal ***     ║
                        ║                                ║
                        ║   ✓  Agregar contacto      1   ║
                        ║   ✍  Modificar contacto    2   ║
                        ║   ✗  Eliminar contacto     3   ║
                        ║   ❓  Buscar contacto       4   ║
                        ║   ✆  Consultar el índice   5   ║
                        ║   ➟  Salir.                6   ║
                        ║                                ║
                        ╚════════════════════════════════╝
          """)

    opcion = input("\t\t\tIngrese una opción: ")

    return opcion

def agregar_contacto(agenda, archivo):
    """ Si no existe, agrega un contacto al diccionario 'agenda' y escribe en 
        el archivo 'datos.txt'. """

    # Verificar si el contacto existe.
    print("\n*** ✓ Agregar: Ingrese los datos del contacto ***\n")
    contacto = ingresar_contacto()
    if contacto_existe(agenda, contacto):
        input("\nEl contacto ya existe.")
    else:
        telefono, email, direccion = ingresar_datos_contacto()
        print("")
        # Agregar contacto al diccionario 'agenda'.
        agenda[contacto] = [telefono, email, direccion]
        # Escribir datos en el archivo.
        apellido, nombre = contacto
        linea = ",".join([apellido, nombre, telefono, email, direccion]) + "\n"
        agregar_linea(linea, archivo)

def modificar_contacto(agenda, archivo):
    """ Modifica los datos de contacto, reingresando sólo aquellos que se 
        desea modificar. """

    # Verificar si el contacto existe.
    print("\n*** ✍ Modificar: Ingrese los datos del contacto ***\n")
    contacto = ingresar_contacto()
    if not contacto_existe(agenda, contacto):
        input("\nEl contacto no existe.")
    else:
        print("\nIngrese los datos nuevos ('Enter' para dejar como está)\n")
        apellido, nombre = ingresar_contacto()
        telefono, email, direccion = ingresar_datos_contacto()

        if apellido == "":
            apellido = contacto[0]
        if nombre == "":
            nombre = contacto[1]
        if telefono == "":
            telefono = agenda[contacto][0]
        if email == "":
            email = agenda[contacto][1]
        if direccion == "":
            direccion = agenda[contacto][2]

        contacto_mod = (apellido, nombre)

        # Borrar contacto antiguo.
        agenda.pop(contacto)
        # Agregar contacto modificado a la agenda.
        agenda[contacto_mod] = [telefono, email, direccion]

        # Escribir Agenda en archivo.
        volcar_datos(agenda, archivo)

def eliminar_contacto(agenda, archivo):

    # Verificar si el contacto existe.
    print("\n*** ✗ Eliminar: Ingrese los datos del contacto ***\n")
    contacto = ingresar_contacto() 
    if not contacto_existe(agenda, contacto):
        input("\nEl contacto no existe.")
    else:
        opcion = input("\n¿Confima que quiere eliminar el contacto (S/N)?: ")
        if opcion.lower() == "s":
            agenda.pop(contacto)
            volcar_datos(agenda, archivo)

def buscar_contacto(agenda):

    print("\n*** ❓ Buscar: Ingrese los datos del contacto ***\n")
    contacto = ingresar_contacto()
    if not contacto_existe(agenda, contacto):
        input("\nEl contacto no existe.")
    else:
        input("\n'Enter' para continuar.")

def listar_contactos(agenda):
    """ Imprime un índice telefónico ordenado alfabéticamente. """

    os.system('clear')

    # Obtiene las claves del diccionario 'agenda'.
    claves = agenda.keys()
    # Crea una lista y las ordena alfabéticamente.
    lista_claves = list(claves)
    lista_claves.sort()

    print("\n" + "*** ✆ Índice Telefónico ***".center(80))

    letra_anterior = ""

    for contacto in lista_claves:
        apellido, nombre = contacto
        # La letra del índice será igual a la primera letra del apellido.
        letra = apellido[0]
        if letra != letra_anterior:
            print("\n\t\t✍  " + letra)
            letra_anterior = letra
        print("\t\t" + (apellido + ", " + nombre).ljust(35) + "☎  " \
              + agenda[contacto][0])
    input()


# Funciones de manejo de archivo.

def cargar_datos(archivo):
    """ Crea un diccionario 'agenda' con los datos del archivo 'datos.txt'.
        El diccionario tiene por clave una tupla con el apellido y el nombre 
        del contacto, y como valor una lista con los datos de teléfono, e-mail
        y dirección del contacto. 
    """

    agenda = {}

    with open(archivo, 'r') as datos:
        for linea in datos:
            # Crear una lista con los datos de cada línea.
            registro = linea.rstrip().split(", ")
            # Unir datos Apellido y Nombre para formar una tupla 'contacto'.
            contacto = (registro[0], registro[1])
            # Crear diccionario con la tupla como clave y el resto de la lista
            # como valor.
            agenda[contacto] = registro[2:]

    return agenda

def volcar_datos(agenda, archivo):
    """ Actualiza el archivo 'datos.txt' con los datos de 'agenda'. Lo usan
        las funciones eliminar_contacto() y modificar_contacto() que no
        pueden simplemente agregar una línea al final. """

    lista = []

    for clave in agenda:
        apellido, nombre = clave
        telefono, email, direccion = agenda[clave]
        linea = ", ".join([apellido, nombre, telefono, email, direccion]) + "\n"
        lista.append(linea)
    
    lista.sort()
    escribir_archivo(lista, archivo)

def escribir_archivo(lista, archivo):
    """ Crea archivo si no existe o escribe una lista en el archivo. """

    with open(archivo, 'w') as datos:
        datos.writelines(lista)

def agregar_linea(linea, archivo):
    """ Agrega una línea al archivo 'datos.txt'. Lo usa la función 
        agregar_contacto() y también sirve para crear el archivo en caso
        de no existir. """

    with open(archivo, 'a') as datos:
        datos.write(linea)


# Programa principal.

def main():

    archivo = 'datos.txt'

    # Si el archivo no existe lo crea.
    if not os.path.isfile(archivo):
        escribir_archivo([], archivo)
        agenda = {}
    # Cargar los datos del archivo 'datos.txt' en el diccionario 'agenda'.
    else:
        agenda = cargar_datos(archivo)

    # Llamar al menú principal.
    opcion = ""
    while opcion != "6":
        opcion = menu_principal()
        os.system('clear')
        if opcion == "1":
            agregar_contacto(agenda, archivo)
        elif opcion == "2":
            modificar_contacto(agenda, archivo)
        elif opcion == "3":
            eliminar_contacto(agenda, archivo)
        elif opcion == "4":
            buscar_contacto(agenda)
        elif opcion == "5":
            listar_contactos(agenda)
        print()

if __name__ == '__main__':
    main()