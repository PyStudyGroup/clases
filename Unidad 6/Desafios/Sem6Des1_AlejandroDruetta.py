#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main():

    capas = []
    desplaza = []

    cantidad = int(raw_input("¿Cuántas capas tendrá el diseño?: "))
    ancho = int(raw_input("¿Cuál será el ancho del patrón?: "))

    for i in range(cantidad):

        while True:

            print "Introduzca el diseño de la capa %d:" % i

            # Crea una guía visual para ayudar al usuario a introducir el diseño
            # de las capas.

            guia(ancho)
            capa = raw_input()

            # Agrega espacios en blanco si la capa no completa la línea y agrega
            # las capas a una lista 'capas'.

            if len(capa) < ancho:
                capa += (ancho - len(capa)) * " "
                break

            elif len(capa) > ancho:
                print "Error: La capa no puede tener longitud mayor que %d." % ancho

            else:
                break

        capas.append(capa)

        # Ingresa los datos de desplazamiento y controla que los valores sean
        # válidos.

        while True:
            desplazamiento = int(raw_input("¿Cuál será el desplazamiento de esta capa (-1, 0, 1)?: "))
            if desplazamiento not in [-1, 0, 1]:
                print "Error: el valor del desplazamiento es inválido."
            else:
                desplaza.append(desplazamiento)
                break

    repite = int(raw_input("¿Cuántas hiladas tendrá el diseño?: "))

    for i in range(repite):

        # Mezcla las capas para cada hilada e imprime.

        hilada = mezcla_capas(capas)
        print hilada

        # Desplaza las capas para la próxima hilada.

        capas = desplaza_capas(capas, desplaza)

def guia(ancho):
    """Guía visual para el ingreso de las capas. Un tope para el inicio y para
    el final y numerado."""

    contador = 1
    guia = ""

    for i in range(ancho):
        if contador > 9:
            contador = 0
        guia += str(contador)
        contador += 1

    tope = "|" + " " * (ancho - 2) + "|"

    print guia
    print tope

def mezcla_capas(capas):
    """Mezcla las capas superponiendo una capa superior a otra inferior. si la
    capa superior tiene espacios en blanco se verá lo que hay en la capa inferior"""

    cantidad = len(capas)
    ancho = len(capas[0])
    fondo = capas[0]

    # Crea una cadena que es el resultado de superponer una capa superior a otra
    # inferior.

    for i in range(cantidad-1):
        hilada = ""
        for ii in range(ancho):

            # Para cada elemento de la capa superior, si es un espacio en blanco
            # selecciona el elemento de la misma posición de la capa inferior.

            if capas[i+1][ii] == " ":
                hilada += fondo[ii]

            # Si no, selecciona el elemento de la capa superior.

            else:
                hilada += capas[i+1][ii]

        # La cadena resultante pasa a ser la capa inferior 'fondo' y se repite
        # el proceso con la capa siguiente.

        fondo = hilada

    return hilada

def desplaza_capas(capas, desplazamiento):
    """Desplaza las capas según el valor almacenado en 'desplazamiento.'"""

    cantidad = len(capas)

    for i in range(cantidad):
        if desplazamiento[i] == -1:

            # Quita el primer caracter y lo agrega al final.
            capas[i] = capas[i][1:] + capas[i][:1]

        elif desplazamiento[i] == 1:

            # Quita el último caracter y lo coloca al principio.
            capas[i] = capas[i][-1:] + capas[i][:-1]

    return capas

main()
