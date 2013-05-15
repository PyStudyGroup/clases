def ordenar(num1,num2):
	if num1 < num2:
		temp = num2
		num2=num1
		num1=temp
	return num1,num2

def main():
	num1 = input("Numero 1: ")
	num2 = input("Numero 2: ")
	num1,num2 = ordenar(num1,num2)
	resto = num1%num2
	if resto==0:
		print "%s es multiplo de %s" %(num1,num2)
	else:
		print "%s no es multiplo de %s" %(num1,num2)


if __name__ == "__main__":
	main()
	
