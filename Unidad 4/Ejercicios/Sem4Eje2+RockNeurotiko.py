def main():
	num1 = input("Numero 1: ")
	num2 = input("Numero 2: ")

	if num1>num2:
		temp=num2
		num2=num1
		num1=temp
	if num1==num2:
		print "Iguales"
	else:
		print "Menos: %s Mayor: %s"%(num1, num2)


if __name__ == "__main__":
	main()
	