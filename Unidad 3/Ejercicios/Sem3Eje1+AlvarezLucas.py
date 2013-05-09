

def tablas(maximo, inicio, fin):

	for x in range(maximo):
		print ""
		x += 1
		
		for y in range(inicio, fin):
			print x, "x", y, "=", x * y

def main():
	
	tabla = input("Hasta que tabla quiere imprimir???? ")
	inicio = input("Número inicial? ")
	fin = input("Número final? ")
	
	fin += 1
	
	tablas(tabla, inicio, fin)
	
if __name__ == "__main__":
	main()

