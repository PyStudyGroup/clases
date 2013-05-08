def imprimirTabla(numero, inicio, fin):
	for i in range(inicio, fin+1):
		print "%s x %s = %s" %(numero, i, numero*i)


def hacerTablas(hasta, inicio, fin):
	for i in range(hasta):
		imprimirTabla(i+1, inicio, fin)
		print "\n"


def main():
	hasta = raw_input("Hasta: ")
	inicio = raw_input("Inicio: ")
	fin = raw_input("Fin: ")

	hacerTablas(int(hasta), int(inicio), int(fin))

if __name__ == "__main__":
	main()

