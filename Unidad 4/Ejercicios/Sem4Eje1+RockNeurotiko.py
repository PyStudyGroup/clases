def main():
	dividendo = input("dividendo: ")
	divisor = input("divisor: ")
	if divisor==0:
		print "No se puede dividor por 0"
	else:
		cociente = int(dividendo/divisor)
		resto = dividendo % divisor
		if resto == 0:
			print "Division perfecta: Cociente: %s" % cociente
		else:
			print "Division NO perfecta: Cociente: %s Resto: %s" %(cociente,resto)


if __name__ == "__main__":
	main()
	