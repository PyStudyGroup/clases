def main():
	total = 1
	num = raw_input("Numero: ")
	for i in range(1,int(num)+1):
		total*=i
	print total

if __name__ == "__main__":
	main()