# -*- coding: utf8 -*-

"""=====================================================================
Autor:                    Emanuel GP
Ubicacion:                Morelos, Mex.
Nombre/Archivo:           Sem1Des2+EmanuelGP.py
Nombre/Programa:          Ciclo Definido "For"
Fecha:                    26/04/2013

Descripcion del Programa.

 *Programar un código que genere la siguiente salida:
    Ingrese un número: 9
    9
    9
    10
    12
    15
    19
    24
    30
    37

>>Nota: La primera línea del presente código, es para que el interprete
        de Python identifique el tipo de codificación que manejará el
        programa durante su ejecución, en este caso es la codificación
        UTF-8. Esto es para que se puedan manejar tildes y letras
        especiales, acentos, etc. Ejemplo: Á, é, ñ, Ñ, etc...

====================================================================="""

print "\t\t\tCiclo Definido 'For'\n"

numRange = input("Ingrese un número entero: ")

for num in range(numRange):
    print numRange
    numRange = numRange + num

print "\n"
