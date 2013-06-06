'''
Ejercicio 5.1 Facturar el uso del un telefono dando la tarifa por segundo y
la duracion de cada comunicacion expresada en horas, minutos y segundos. 
Dando como resultado la duracion en segundos de cada comunicacion y su costo.
Resolver usando: 
1.Ciclo definido
2.Ciclo interactivo
3.Ciclo centinela
4.Ciclo "infinito" que se rompe"
'''

#Ciclo Centinela
def tarifa():
	opcion = raw_input("Ingrese 'si' para empezar o 'x' para terminar: ")
	while opcion<>'x':
		comunicacion = input("Cuantas comunicaciones son?: ")
		print "-"*20
		for x in range(comunicacion):
			#------- pedimos datos ---------	
			precioseg = input("Cual es la tarifa por segundo: ")
			horas = input("Cuantas horas?: ")
			minutos = input("Cuantos minutos?: ")
			segundos = input("Cuantos segundos?: ")
			#----- hacemos los calculos -----
			total_tiempo = (horas*3600) + (minutos*60) + segundos
			total_costo = total_tiempo * precioseg
			pesos = int(total_costo)
			centavos = int((pesos-total_costo)*10)
			#--------- imprimimos -----------
			print "La comunicacion dura:",total_tiempo, "segundos"
			print "El precio total es de:",pesos,"pesos con:",centavos,"centavos"
			print "-"*20

		opcion = raw_input("Ingrese (si) para seguir o 'x' para terminar: ")	

tarifa()