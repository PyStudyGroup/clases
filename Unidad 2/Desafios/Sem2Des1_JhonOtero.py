# -*- coding: utf-8 -*-
# Author : Jhon Otero

def bintodecimal():
	#Inicalizamos la varable sum
	decimal = 0
	#Pedimos introducir un numero en binario
	bin = raw_input("Ingrese un numero binario: ")
	#Creamos un ciclo para que recorra cada numero ingresado
	for i in range(len(bin)):
		#Verificamos si el numero contiene el binario 1
		if bin[-(i+1)] == '1':
			#Si lo contiene hacemos la suma de la potencia sucesivas de 2
			#Ejemplo  128 +  64 +  32 +  16 +  8  +  4  +  2   +  1
			# 		  2^7 + 2^6 + 2^5 + 2^4 + 2^3 + 2^2 + 2^1  + 2^0

			decimal += 2**i

	return decimal			

decimal = bintodecimal()

print decimal


