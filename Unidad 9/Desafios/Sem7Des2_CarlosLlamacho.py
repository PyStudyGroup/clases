# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 15:33:05 2013

@author: cllamach

Desafio 2 - Grupo de Estudio Python - Unidades 8 y 9.

Crear un diccionario con los participantes de un curso, ingresando:

Nombre.
Apellido.
Edad.
Teléfono.
Correo Electrónico.
Localidad.

El programa nos debe permitir gerenciar esa lista agregando o eliminando 
participantes y también corrigiendo datos. Generar informes permitiendo al
usuario elegir qué columnas (Nombre, Apellido, etc.) quiere imprimir en pantalla.
"""

from collections import OrderedDict
import sys

def menu(agenda):
	
	#Menu con las opciones. 1-6
	print("-"*25)
	print("Menu: ")
	print("-"*25)
	print("1-Agregar datos.")
	print("2-Ver datos.")
	print("3-Eliminar datos.")
	print("4-Editar datos.")
	print("5-Informes.")
	print("6-Salir.")
	print("-"*25)
	opcion = int(input("Seleccione la opcion deseada(1-6): "))
	
	while opcion not in range(1,7):
		opcion = int(input("Su seleccion no es una opcion valida, intente nuevamente(1-6): "))
	
	#Funciones core de la agenda. Cada eleccion indicara el flujo.
	#Exceptuando la funcion 6 que sale del programa, todas regresan al menu.	
	if opcion == 1:
		agregar(agenda)
		menu(agenda)
	elif opcion == 2:
		ver(agenda)
		menu(agenda)
	elif opcion == 3:
		eliminar(agenda)
		menu(agenda)
	elif opcion == 4:
		corregir(agenda)
		menu(agenda)
	elif opcion == 5:
		informes(agenda)
		menu(agenda)
	elif opcion == 6:
		sys.exit()

def agregar(agenda):
	
	siguiente = True
	
	#Loop que recoge datos hasta que se indique lo contrario.
	while siguiente:
		print("Datos a agregar al diccionario: ")
		print("-"*25)
		nombre = str(input("Nombre: "))
		apellido = str(input("Apellido : "))
		edad = int(input("Edad: "))
		telefono = int(input("Telefono: "))
		email = str(input("Email: "))
		localidad = str(input("Localidad: "))
		print("-"*25)
		
		agenda.append(OrderedDict([("nombre", nombre), ("apellido",apellido),("edad",edad), ("telefono",telefono), ("email",email),("localidad",localidad)]))			
		
		seguir = str(input("Quiere ingregsar otra persona a la agenda(Y/N): "))
		if seguir == "N" or seguir == "N".lower:
			siguiente = False
			
	return agenda
	
def ver(agenda):
	#Muestra todos los datos almacenados en la agenda.	
	for entrada in agenda:
		print("#"*50)
		for key in entrada:
			print(str(key) + ": " + str(entrada.get(key)))
	

def eliminar(agenda):
	
	print("Entradas en la agenda: ")
	#Muestra el indice junto con el nombre y el apellido de cada persona de la agenda.
	for entrada in agenda:
		print(str(agenda.index(entrada)) + " - "+ str(entrada.get("nombre")) +" "+ str(entrada.get("apellido")))
	print("*"*25)
	#Se selecciona el indice que se desea borrar.
	eliminar = int(input("Seleccione la que quiera eliminar: "))
	#Se asegura que el indice este correcto.
	while eliminar not in range(0, len(agenda)+1):
		eliminar = int(input("Seguro que eligio bien? Intente nuevamente: "))
	#Se saca ese diccionario del la agenda.
	agenda.pop(eliminar)
	print("El dato fue eliminado.")	
			
def corregir(agenda):
	print("Entradas en la agenda: ")
	#Muestra la posicion en la lista, nombre y apellidos de los diccionarios.
	for entrada in agenda:
		print(str(agenda.index(entrada)) + " - "+ str(entrada.get("nombre")) + " "+ str(entrada.get("apellido")))
	print("*"*25)
	#Se hace seleccion de la que se quiere corregir.
	corregir = int(input("Seleccione la entrada que quiere corregir: "))
	#Se verifica que sea correcta la seleccion.
	while corregir not in range(0, len(agenda)+1):
		corregir = int(input("Seguro que eligio bien? Intentelo nuevamente: "))
	print("*"*25)
	#Muestra los datos de la entrada seleccionada.
	print("Datos disponibles")
	#Esta list comprehension recorre el objeto Keys.Items y crea una lista con todas las llaves del diccionario en cuestion.
	llaves = [x for x in agenda[corregir].keys()]
	#Recorremos la lista, para seleccionar el dato que querremos corregir.
	#Muestra el indice dentro de la lista y el valor.
	for llave in llaves:
		print(str(llaves.index(llave))+" - "+str(llave))
	#El usuario debe seleccionar el indice que quiere corregir.
	eleccion = int(input("Que datos de la agenda quiere corregir: ")) 
	#Se verifica que el indice este en la lista.
	while eleccion not in range(0, len(llaves)+1):
		eleccion = int(input("Seguro que eligio bien? Intentelo nuevamente: "))
	#Esto llama a la lista que contiene los diccionarios usando el indice que se quiere corregir, es decir el diccionario que queremos cambiar.
	#Luego dentro del diccionario usa la lista de llaves que tenemos y la eleccion para pasar al diccionario el valor de la llave que queremos modificar.
	#Finalemente se pide la modificación y listo.
	agenda[corregir][llaves[eleccion]] = input("Introduzcac la correccion deseada: ")
	print("Dato corregido")

def informes(agenda):
	
	print("Informes")
	print("Campos disponibles: ")
	#Busca las llaves del primer diccionario, para mostrarlas como ejemplo.
	#Todos los diccionarios tienen las mismas llaves.
	llaves = [llave for llave in agenda[0]]
	for llave in llaves:
		print(str(llaves.index(llave)) + " - "+ str(llave))
	print("*"*25)
	continuar = True
	selecciones = []
	#Despues de mostrar los campos, pedimos que se seleccione uno y se va almacenando en una lista.
	while continuar:		
		selecciones.append(int(input("Seleccione un campo para presentar en el informe: ")))
		continuamos = input("Quiere añadir otro campo?(Y/N): ")
		if continuamos == "N" or continuamos == "n":
			continuar = False
	print("*"*25)
	print("Ha solicitado un informe con los siguientes campos: ")
	#Mostramos los campos que tendra el informe.
	for i in selecciones:
		print(str(llaves[i]))
	print("*"*25)
	print("Informe: ")
	#Se recorre cada una de las llaves seleccionadas.
	for seleccion in selecciones:
		#Se muestran todos los valores de cada diccionario para la llave correspondiente.
		for dicc in agenda:
			print(str(dicc[llaves[seleccion]]))
		print("-"*50)
	print("Informe presentado.")				
		
def main():
	
	#Inicializar la agenda.
	agenda = []
	
	#Cargar el menu usando la agenda creada.
	menu(agenda)
	
if __name__=="__main__":
	main()
