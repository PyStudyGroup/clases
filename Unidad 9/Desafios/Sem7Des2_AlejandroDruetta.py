#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main():

    nomina = {0:["Druetta", "Alejandro", 41, "11-97051-9988", "aledruetta@gmail.com", "São Paulo"]}
    codigo = 1

    while True:

        print """*** Menú Principal ***

    1. Ingresar
    2. Eliminar
    3. Modificar
    4. Visualizar
    5. Salir
    """

        opcion = raw_input("Opción: ")
        print

        if opcion == "1":
            nomina = ingresa(nomina, codigo)
            codigo += 1
        elif opcion == "4":
            visualizar(nomina)
        elif opcion == "5":
            break
        else:
            print "Opción inválida."

def ingresa(nomina, codigo):

    apellido = raw_input("Apellido: ")
    nombre = raw_input("Nombre: ")
    edad = int(raw_input("Edad: "))
    telefono = raw_input("Teléfono: ")
    email = raw_input("e-mail: ")
    localidad = raw_input("Localidad: ")

    nomina[codigo] = [nombre, apellido, edad, telefono, email, localidad]

    return nomina

def visualizar(nomina):

    while True:

        print """*** Menú Informes ***

    1. Por Nombres y Apellidos
    2. Por Teléfonos y E-mails
    3. Por Localidades
    4. Por Edades
    5. Salir
    """

        opcion = raw_input("Opción: ")
        print

        if opcion == "1":
            print "Cod.", "Alumnos", "\n"
            for i in nomina:
                print "%4d %s" % (i, (nomina[i][0] + ", " + nomina[i][1]))
        elif opcion == "2":
            print "Cod.", "Teléfono", (2 * "\t"), "E-mail"
            for i in nomina:
                print "%4d %s" % (i, (nomina[i][3] + "\t" + nomina[i][4]))
        elif opcion == "3":
            print "Cod.", "Localidad"
            for i in nomina:
                print "%4d %s" % (i, (nomina[i][5]))
        elif opcion == "4":
            print "Cod.", "Edad"
            for i in nomina:
                print "%4d %s" % (i, (nomina[i][2]))
        elif opcion == "5":
            break
        else:
            print "Opción inválida."

        print
        raw_input("Presione 'Enter' para volver al menú.")

main()
