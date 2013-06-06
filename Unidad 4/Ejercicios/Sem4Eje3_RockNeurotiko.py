def main():
	num1 = input("Anho actual: ")
	num2 = input("Anho rand: ")
	dif = abs(num1-num2)
	if dif == 1:
		anho = "anho"
		may="Ha pasado"
		men="Falta"
	else:
		anho="anhos"
		may="Han pasado"
		men="Faltan"

	if num1>num2:
		print "%s: %s %s hasta %s" %(may,num1-num2, anho, num1)
	elif num1==num2:
		print "Iguales"
	else:
		print "%s: %s %s hasta %s" %(men, num2-num1, anho, num2)


if __name__ == "__main__":
	main()
	
