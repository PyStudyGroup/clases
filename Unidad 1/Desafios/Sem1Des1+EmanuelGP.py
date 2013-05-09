# -*- coding: utf8 -*-

"""=====================================================================
Autor:                    Emanuel GP
Ubicacion:                Morelos, Mex.
Nombre/Archivo:           Sem1Des1+EmanuelGP.py
Nombre/Programa:          Calcula Edad
Fecha:                    22/04/2013

Descripcion del Programa.

 *Escribir un pequeño programa donde:
- Se ingresa el año en curso.
- Se ingresa el nombre y el año de nacimiento de tres personas.
- Se calcula cuántos años cumplirán durante el año en curso.
- Se imprime en pantalla.

>>Nota: La primera línea del presente código, es para que el interprete
        de Python identifique el tipo de codificación que manejará el
        programa durante su ejecución, en este caso es la codificación
        UTF-8. Esto es para que se puedan manejar tildes y letras
        especiales, acentos, etc. Ejemplo: Á, é, ñ, Ñ, etc...

====================================================================="""

print "\t\t\tCalcula Edad\n"
print "El siguiente programa calculará la edad que cumpliran tres personas  "
print "durante el presente año, para lo cual se deberá ingresar al programa "
print "el año actual en curso, el nombre y año de nacimiento de cada persona"
print "y al terminar los calculos, estos se mostraran en pantalla...\n"

anioActual = input("Introduce el año en curso: ")
persona1 = raw_input("Escribe el nombre de la persona 1: ")
anio1 = input("Ingresa el año de nacimiento de la persona 1: ")
persona2 = raw_input("Escribe el nombre de la persona 2: ")
anio2 = input("Ingresa el año de nacimiento de la persona 2: ")
persona3 = raw_input("Escribe el nombre de la persona 3: ")
anio3 = input("Ingresa el año de nacimiento de la persona 3: ")

anios1 = anioActual - anio1
anios2 = anioActual - anio2
anios3 = anioActual - anio3

print "\n"
print persona1, "cumplirá ", anios1, " años."
print persona2, "cumplirá ", anios2, " años."
print persona3, "cumplirá ", anios3, " años.\n"
