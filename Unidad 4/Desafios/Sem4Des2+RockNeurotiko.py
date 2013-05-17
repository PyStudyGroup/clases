from Test import test

def match_ends(words):
	count = 0
	for i in words:
		if len(i) >= 2 and i[0] == i[-1]:
			count +=1
	return count

def main():
	print 'match_ends'
	test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
	test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
	test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

if __name__=="__main__":
	main()
