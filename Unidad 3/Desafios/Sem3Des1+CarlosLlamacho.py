#Grupo de estudio de Python G+.

#Unidad 3 - Desafio 1

"""es_primo
Un número primo es un entero positivo mayor que 1 que no tiene divisores positivos distintos al 1 y a sí mismo.
En otras palabras, si deseas saber si un número en una variable x es primo, entonces ningún otro número debería poder dividir x con residuo cero aparte del 1 y de x.
Si hay un número entre 1 y x que pueda dividirlo con residuo cero, entonces x no es primo.
Instrucciones
Escribe una función es_primo que tome un número x como entrada y devuelva el booleano Verdadero si x es primo y Falso si no lo es."""

#Carlos Llamacho

def esprimo(numero):
	"""Recibe un numero positivo mayor que 2 y verifica si es primo o no, sin usar ifs."""
	contador = 2
	
	resultado = True
	
	#Loop principal. Corre hasta que el contador sea numero - 1.
	while contador < numero:
		#Hace la division.
		resto = numero % contador
		
		#Mientras la division no sea 0, se salta esta parte completamente.
		while resto == 0:
			#Si la division es 0, esto entrara en un loop infinito.
			resultado = False
			#por eso rompemos el loop con break
			break
		
		contador += 1
	return resultado

def criba(numero):
	
	#List comprehension.
	numeros = [num for num in range(2, numero + 1)]
	
	#Primer numero de la lista.
	primero = numeros[0]
	
	#Listado de resultado.
	primos = []
	
	#Loop principal.
	while primero < numero:
		primos.append(primero)
		
		for item in numeros:
			#Si es primo, lo saca del listado.
			if item % primero == 0:
				numeros.remove(item)
		#Este try se añadio porque llegaba al final de la lista, intentaba asignar y estaba vacia.
		try:
			numeros.remove(numeros[0])
			primero = numeros[0]
		except(IndexError) as error:
			break
			
		
	return primos
		
			
			
					


if __name__=="__main__":
	
	numero = int(input("Introduce un numero positivo mayor a 2: "))
	
	print(criba(numero))
