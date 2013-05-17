from Test import test

def desglosar(numero):
	desglose=[]
	VALORES=[500,200,100,50,20,10,5,2,1]
	for valor in VALORES:
		cociente = int(numero/valor)
		if cociente >= 1:
			desglose.append((cociente,valor))
			numero -= cociente*valor
	return desglose

def imprimirDesglose(desglose):
	for i in desglose:
		plural=""
		tipo="billete"
		if i[0] > 1: plural="s"
		if i[1] < 5: tipo="moneda"

		print "%s %s%s de %s euros." % (i[0], tipo, plural, i[1])

def main():
	test(desglosar(20),[(1,20)])
	test(desglosar(40),[(2,20)])
	test(desglosar(434),[(2,200),(1,20),(1,10),(2,2)])

	imprimirDesglose(desglosar(434))


if __name__ == "__main__":
	main()


