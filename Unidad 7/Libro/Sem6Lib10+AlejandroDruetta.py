#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Ejercicio 10 Unidad 7 Libro.
# Autor:    Alejandro Druetta
# Fecha:    29/05/13
# Versión:  Python 2.7.4

def main():

    mensaje = raw_input("mensaje: ")

    maximo = int(raw_input("Máximo palabra corta: "))
    precio_cortas = int(raw_input("Precio palabra corta: "))
    precio_largas = int(raw_input("Precio palabra larga: "))

    telegrama, cortas, largas = a_palabras(mensaje, maximo)
    print
    print "Telegrama: '%s'" % telegrama
    print "Precio palabras cortas: $ %d" % (cortas * precio_cortas)
    print "Precio palabras largas: $ %d" % (largas * precio_largas)

def a_palabras(mensaje, maximo):
    """ Recibe el mensaje en bruto y lo acomoda al formato de telegrama. """

    mensaje = mensaje.split()

    indice = 0
    cortas = 0
    largas = 0
    for i in mensaje:

        if len(i) > 1 and i[-1] == ".":
            mensaje[indice] = i[:-1]
            mensaje.insert(indice+1, "STOP")
        elif i == ".":
            mensaje[indice] = "STOP"

        if len(i) <= maximo:
            cortas += 1
        elif i != "STOP":
            largas += 1

        if len(i) > 5:
            mensaje[indice] = i[:5] + "@"

        indice += 1

    if mensaje[-1] == "STOP":
        mensaje[-1] = "STOPSTOP"
    else:
        mensaje.append("STOPSTOP")

    return " ".join(mensaje), cortas, largas

main()
