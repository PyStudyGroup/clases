def main():
	CM2KM = 100000
	CM2M = 100
	cm = input("Centimetros: ")
	km = int(cm/CM2KM)
	cm -= km*CM2KM
	m = int(cm/CM2M)
	cm -= m*CM2M

	if km>0:
		if m>0:
			if cm>0:
				print "%s km, %s m y %s cm" %(km,m,cm)
			else:
				print "%s km y %s m" %(km,m)
		else:
			if cm>0:
				print "%s km y %s cm" %(km,cm)
			else:
				print "%s km" %(km)
	else:
		if m>0:
			if cm>0:
				print "%s m y %s cm" %(m,cm)
			else:
				print "%s m" %(m)
		else:
			if cm>0:
				print "%s cm" %(cm)
			else:
				print "Has introducido 0 ¬¬"


if __name__ == "__main__":
	main()
