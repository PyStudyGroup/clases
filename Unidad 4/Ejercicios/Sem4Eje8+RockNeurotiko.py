from math import sqrt
def main():
	a = input("coeficiente 1 (a): ")
	b = input("coeficiente 2 (b): ")
	c = input("coeficiente 3 (c): ")
	discrim = b**2 - 4*a*c
	if discrim<0:
		print "Sin solucion real"
	elif discrim == 0:
		print "Doble solucion unica: x=%s" %(-(b/2*a))
	else:
		print "Doble solucion: x1=%s x2=%s" %(  (-b+sqrt(discrim))/(2*a), (-b-sqrt(discrim))/(2*a)  )



if __name__ == "__main__":
	main()
	
