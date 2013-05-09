def isPrime(n):
	if n==2: return True #Si es dos es primo
	if n<2 or n%2==0: return False #Si es menor o divisible por dos, no lo es
	return not any(n % x==0 for x in xrange(3, int(n**0.5) + 1, 2))
        #Se ha usado xrange por si el numero es muy grande
        #Ya que xrange es mas eficiente que range


def main():
	n = raw_input("Introduzca el numero: ")
	if isPrime(int(n)): print("Es primo")
	else: print("No es primo")

if __name__ == "__main__":
	main()
