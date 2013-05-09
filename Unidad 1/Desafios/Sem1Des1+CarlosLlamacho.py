#Grupo de estudio Python
#Semana 1 - Desafio 1

"""Escribir un pequeno programa donde:
-Se ingrese el año en curso.
-Se ingrese el nombre y el año de nacimiento de tres personas.
-Se calcule cuantos años cumplirarn durante el año en curso.
-Se imprima en pantalla"""

#Ejercicio realizado por:
#Carlos Llamacho


def desafio1():
	"""Programa que calcula la edad de 3 personas basada en el año actual y su fecha de nacimiento"""
	
	año = input("Ingrese el año en curso: ")
	nombres = []
	años =[]
	edades = []
		
	for counter in range(3):
		nombres.append(input("Ingrese un nombre: "))
		años.append(input("Ingrese el año de naciemiento de esa persona: "))
		edades.append(str(int(año) - int(años[counter])))
		print(nombres[counter] + "\t|" + años[counter] + "\t|" + edades[counter] + "\n")
	

	

if __name__=="__main__":
	desafio1()

