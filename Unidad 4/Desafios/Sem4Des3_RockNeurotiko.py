from Test import test

def front_x(words):
  lisX = []
  lisXSort = []

  for i in sorted(words):
    if i[0] != "x":
      lisXSort.append(i)
    else:
      lisX.append(i[1:])
  
  lisX = sorted(lisX, reverse=True)
  for i in lisX:
    lisXSort.insert(0,"x"+i)
  return lisXSort


def main():
  print 'front_x'
  test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

if __name__=="__main__":
  main()