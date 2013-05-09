def binario_entero():
	numero = input("Ingresa el numero binario?: ")                               
	largo = len(str(numero))			                           
	total = 0											  						   
	contador = 1

	for i in range(largo):
		constante = 1
		numero = str(numero)
		basedos = 2 ** i
		suma = basedos * int(numero[largo-contador])
		total = total + suma
		contador = contador + constante
	print "Del numero binario ingresado: %s su numero entero es: %s" % (numero, total)

binario_entero()