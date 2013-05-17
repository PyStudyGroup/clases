from Test import test

def unicos(values):
    a=[]
    for value in values:
            if value not in a:
                    a.append(value)
    return a

def main():
    print 'unicos'
    test(unicos([]),[])
    test(unicos([1,3,1,3]),[1,3])
    test(unicos([1,3,5,6,6,5,3,1,9711]),[1,3,5,6,9711])

if __name__=="__main__":
    main()
