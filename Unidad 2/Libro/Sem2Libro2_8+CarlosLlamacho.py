#Grupo de estudio de Python G+.

#Unidad 2 - Ejercicio Libro 2.8

"""Escribir un programa que use un ciclo definido con rango numérico, 
que averigue a cuántos amigos quieren saludar, les pregunte los nombres 
de esos amigos/as, y los salude."""

#Carlos Llamacho

def saludar():
	#Recoge la cantidad de personas a saludar.
	amigos = int(input("A cuantos amigos quiere saludar: "))
	
	#Loop que los saluda a todos.
	for i in range(1, amigos+1):
		
		#Pregunta el nombre.
		nombre = str(input("Cual es tu nombre: "))
		#Saluda.
		print("Hola " + nombre + ". Bienvenido/a.")
		print("*" * 25)

if __name__=="__main__":
	saludar()
