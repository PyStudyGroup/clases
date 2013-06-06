def main():
	num1 = input("Numero 1: ")
	num2 = input("Numero 2: ")
	num3 = input("Numero 3: ")
	dif=0
	for i in [num1,num2,num3]:
		for j in [num1,num2,num3]:
			if i==j:
				dif+=1
	dif -= 3 #Quitamos los obvios num1==num1,num2==num2,num3==num3

	if dif == 6: #Es 6 porque hay comparaciones repetidas
		print "Los 3 iguales"
	elif dif==2:
		print "uno de los numeros dos veces"
	else:
		print "ninguno igual"

if __name__ == "__main__":
	main()
	
