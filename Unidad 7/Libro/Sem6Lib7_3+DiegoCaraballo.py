#-*- coding: UTF-8 -*-

"""Ejercicio 7.3. Cartas como tuplas.
a) Proponer una representación con tuplas para las cartas de 
la baraja francesa.
b) Escribir una función poker que reciba cinco cartas de la baraja 
francesa e informe (devuelva el valor lógico correspondiente) si 
esas cartas forman o no un poker (es decir que hay 4 cartas con el 
mismo número)."""

import random

def main():
	cartas_francesas = ("1 de trebol", "2 de trebol", "3 de trebol", "4 de Trebol", 
	"5 de trebol", "6 de trebol", "7 de trebol", "8 de trebol", "9 de trebol",
    "10 de trebol", "11 Valet de trebol", "12 Dame de trebol", "13 Roi de trebol","1 de diamante",
    "2 de diamante", "3 de diamante", "4 de diamante", 
    "5 de diamante", "6 de diamante", "7 de diamante", "8 de diamante", "9 de diamante",
    "10 de diamante", "11 Valet de diamante", "12 Dame de diamante", "13 Roi de diamante",
    "1 de corazon", "2 de corazon", "3 de corazon", "4 de corazon", 
    "5 de corazon", "6 de corazon", "7 de corazon", "8 de corazon", "9 de corazon",
    "10 de corazon", "11 Valet de corazon", "12 Dame de corazon", "13 Roi de corazon","1 de picas",
    "2 de picas", "3 de picas", "4 de picas", 
	"5 de picas", "6 de picas", "7 de picas", "8 de picas", "9 de picas",
    "10 de picas", "11 Valet de picas", "12 Dame de picas", "13 Roi de picas")
 
	c1 = random.choice(cartas_francesas)
	c2 = random.choice(cartas_francesas)
	c3 = random.choice(cartas_francesas)
	c4 = random.choice(cartas_francesas)
	c5 = random.choice(cartas_francesas)

	n1 = 0
	n2 = 0
	n3 = 0
	n4 = 0
	n5 = 0

	n1 = int(c1[0:2])
	n2 = int(c2[0:2])
	n3 = int(c3[0:2])
	n4 = int(c4[0:2])
	n5 = int(c5[0:2])


def poker (carta1, carta2, carta3, carta4, carta5):
	if carta1 == carta2 and carta1 == carta3 and carta1 == carta4 and carta1 == carta5:
		
	
	



	


