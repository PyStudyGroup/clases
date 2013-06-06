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
#Ciclo Definido.-
def tarifa():
	#------ Declaramos variable comunicacion -----
	comunicacion = input("Cuantas comunicaciones son: ")
	
	while comunicacion >0:
		#------- pedimos datos ---------
		print "-"*20
		precioseg = input("Cual es la tarifa por segundo: ")
		horas = input("Cuantas horas: ")
		minutos = input("Cuantos minutos: ")
		segundos = input("Cuantos segundos: ")
		print "-"*20
		#----- hacemos los calculos -----
		total_tiempo = asegundos (horas, minutos, segundos)
		total_costo = total_tiempo * precioseg
		#--------- imprimimos -----------
		print "La comunicacion dura:",total_tiempo, "segundos"
		print "El precio total es de:",int(total_costo),"pesos con", acentavos(total_costo), "centavos"
		comunicacion -= 1

def asegundos (hors, mins, segs) :
	segsal = 3600*hors + 60*mins + segs
	return segsal


def acentavos(cost) :
	centavos = int(round((cost%1)*100))
	return centavos
tarifa()