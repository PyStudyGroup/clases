maximo = input("Tamanho maximo: ")
b1 = input("Tamanho de barra1: ")
b2 = input("Tamanho de barra2: ")
b3 = input("Tamanho de barra3: ")
b4 = input("Tamanho de barra4: ")

print ""
print "El maximo alcance de la barra es: ", maximo

pos = 0
barra_vacia = "    "
barra_llena = "----"

print "+"*23	

for x in range(maximo):
	
	pos = maximo - x
	
	if pos <= b1:
		c1 = barra_llena
	else:
		c1 = barra_vacia

	if pos <= b2:
		c2 = barra_llena
	else:
		c2 = barra_vacia

	if pos <= b3:
		c3 = barra_llena
	else:
		c3 = barra_vacia

	if pos <= b4:
		c4 = barra_llena
	else:
		c4 = barra_vacia
	print "+", c1, c2, c3, c4, "+"


print "+  b1   b2   b3   b4  +"
print "+"*23	



raw_input()