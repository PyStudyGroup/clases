#! /usr/bin/env python
# -*- coding: utf-8 -*-

def main():
	
	encurso = input("En qué año estamos: ")
	print ""
	nombre1 = input("Ingrese un nombre entre comillas: ")
	anio1 = input("Cuándo nació esta persona?: ")
	edad1 = encurso - anio1
	print ""
	nombre2 = input("Ingrese un nombre entre comillas: ")
	anio2 = input("Cuándo nació esta persona?: ")
	edad2 = encurso - anio2
	print ""
	nombre3 = input("Ingrese un nombre entre comillas: ")
	anio3 = input("Cuándo nació esta persona?: ")
	edad3 = encurso - anio3
	print ""
	print "Este año", nombre1, "cumple", edad1
	print "Este año", nombre2, "cumple", edad2
	print "Este año", nombre3, "cumple", edad3

main()
