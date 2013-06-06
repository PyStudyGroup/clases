def saludar_amigos():

	#declaramos una variable "amigos" con formato de lista vacia, 
	#para almacenar los nombres de nuestros amigos	
	amigos = [] 				
	print ""

	#declaramos una variable numero y le asignamos el numero de
	#amigos a saludar
	numero = input("Cuantos amigos quieres saludar: ")
	print ""

	#hacemos un bucle "for" para almacenar los "nombres" de nuestros amigos
	#en la variable amigos
	for n in range(numero):
		nombres = raw_input("Escribe el nombre de tus amigos: ")
		amigos.append(nombres)
	
	print "------------------------------"

	#hacemos un bucle "for" que recorra el numero de amigos y que imprima el
	#saludo segun recorra la lista (amigos)
	for x in range(numero):
		print "Hola " + amigos[x]

saludar_amigos()