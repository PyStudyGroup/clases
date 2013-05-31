#! /usr/bin/env python
# -*- coding: utf-8 -*-

# @autor: Diego Caraballo
# @date: 26/05/13
# @version: python 2.7.4
# Grupo Estudio Python

"""Ejercicio 6.7. En el punto 6 (Mantenimiento) usamos una variable 
que guardara el valor de la cantidad de dígitos para no tener que 
cambiarlo todas las veces. ¿Cómo harían para evitar esta variable 
usando la función len(cadena)?"""

# ARCHIVO: mastermind5.py

# modulo que va a permitir elegir numeros aleatoriamente
import random

# el conjunto de simbolos validos en el codigo
digitos = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9")

# "elegimos" el codigo
cadena = "xx"
cant_digitos = len (cadena)
codigo = ""
for i in range(cant_digitos):
	candidato = random.choice(digitos)
	# vamos eligiendo digitos no repetidos
	while candidato in codigo:
		candidato = random.choice(digitos)
	codigo = codigo + candidato

# iniciamos interaccion con el usuario
print "Bienvenido/a al Mastermind!"
print "Tenes que adivinar un numero de", cant_digitos, \
"cifras distintas"
propuesta = raw_input("Que codigo propones?: ")


# procesamos las propuestas e indicamos aciertos y coincidencias
intentos = 1
while propuesta != codigo and propuesta != "Me doy":
	intentos = intentos + 1
	aciertos = 0
	coincidencias = 0


	#recorremos la propuesta y verificamos en el codigo
	for i in range(cant_digitos):
		if propuesta[i] == codigo[i]:
			aciertos = aciertos + 1
		elif propuesta[i] in codigo:
			coincidencias = coincidencias + 1
	print "Tu propuesta (", propuesta, ") tiene", aciertos, \
			"aciertos y ", coincidencias, "coincidencias."
	# pedimos siguiente propuesta
	propuesta = raw_input("Propone otro codigo: ")
if propuesta == "Me doy":
	print "El codigo era", codigo
	print "Suerte la proxima vez!"
else:
	print "Felicitaciones! Adivinaste el codigo en", \
	intentos, "intentos."
