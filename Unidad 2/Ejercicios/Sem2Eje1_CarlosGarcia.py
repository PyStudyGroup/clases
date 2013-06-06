''' Escribir un programa que calcule el costo total de una compra de libros'''

def total_libros():
	costo = 0
	titulos = ""
	print ""
	libros = input("Cuantos libros compra: ")
	interes = input ("Que taza de interes(%): ")
	print "-"*45
	print ""

	for n in range(libros):
		nombres = raw_input("Escribe los nombres de los libros: ")
		titulos += nombres
		precio = input("Cual es su precio($): ")
		costo += precio
		print "_"*45
		print ""

	interes_solo = costo * (interes*.01)
	interes_total = interes_solo + costo

	print "El numero de libros comprados es de: " + str(libros)
	print "-" * 45
	print "El total del valor de los libros es($): " + str(costo)
	print "-" * 45
	print "El valor total de los impuestos es($): " + str(interes_solo)
	print "-" * 45
	print "El valor total es de($): " + str(interes_total)





total_libros() 