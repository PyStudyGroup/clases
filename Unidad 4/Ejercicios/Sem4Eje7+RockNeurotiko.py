def main():
	a = input("coeficiente 1 (a): ")
	b = input("coeficiente 2 (b): ")
	if a == 0 and b!=0:
		print "No hay solucion"
  elif a==0 and b==0:
    print "Eso no es una funcion"
  else:
		print "Solucion: %s" %(-b/a)


if __name__ == "__main__":
	main()
	
