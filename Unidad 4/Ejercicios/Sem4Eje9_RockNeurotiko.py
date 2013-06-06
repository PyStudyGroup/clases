from math import pi as PI

def triangulo(base,altura):
	return (base*altura)/2

def area(radio):
	return PI*(radio**2)

def main():
	aCalcular = raw_input("(C)irculo o (T)riangulo?: ")
	if aCalcular.lower() == "t":
		base = input("Base: ")
		altura = input("Altura: ")
		print "Superficie Triangulo: %s" % triangulo(base,altura)
	elif aCalcular.lower() == "c":
		radio = input("Radio: ")
		print "Superficie circulo: %s" % area(radio)
	else:
		print "WTF?"




if __name__ == "__main__":
	main()
	
