'''
Created on 24/04/2013

@author: michael
'''
def rombo():
    n=input("Ingresa un numero:",)
    t=n
    for i in range(n):
        for j in range(t):
            print " ",
        for k in range(-1,i):
            k+=2
            print k,
        for s in range(i,0,-1):
            print s,
        print ""
        t-=1
    d=n-2
    for i in range(1,n):
        for i in range(-1,i):
            print " ",
        for s in range(1,n):
            print s,
        for a in range(d,0,-1):
            print a,
        n-=1
        d-=1
        print ""
            
rombo()