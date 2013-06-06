def funcionRara(a,b,c,d):
	return a*b, c/d, b-c

def main():
	a = input("numero 1: ")
	b = input("numero 2: ")
	c = input("numero 3: ")
	d = input("numero 4: ")

	f1,f2,f3 = funcionRara(a,b,c,d)

	print "%s , %s , %s" % (f1,f2,f3)

if __name__ == "__main__":
	main()
