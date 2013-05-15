def main():
	num1 = input("anho: ")

	if num1%400==0:
		print "Es bisiesto por ser multiplo de 400"
	elif num1%100==0:
		print "No lo es por ser multiplo de 100"
	elif num1%4==0:
		print "Es bisiesto por ser multiplo de 4"
	else:
		print "No lo es"

if __name__ == "__main__":
	main()
	