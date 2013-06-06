# -*- coding: utf-8 -*-

#Desafio 2 de la semana #4

"""Dada una lista de strings, la funcion devuelve el contador del
 numero de strings donde la longitud del string es 2 o 
 mayor y el primer y el ultimo caracter del string son iguales."""
 
 #Carlos Llamacho
 
def iguales(datos): 
	resultado = 0
	for item in datos:
		if len(item) >= 2:
			if item[0] == item[-1]:
				resultado += 1
				 
	return resultado

if __name__=="__main__":
	print(iguales(["",  "x", "xy", "xyx", "xx"]))
	print(iguales(["ana", "tia", "dud", "ditto", "FiF", "Fif"]))
