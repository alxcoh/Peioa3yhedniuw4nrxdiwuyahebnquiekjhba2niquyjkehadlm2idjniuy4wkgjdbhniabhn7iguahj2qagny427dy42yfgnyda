'''
Created on Dec 22, 2013

@author: alxcoh
'''
from decimal import *
getcontext().prec = 1
countUpTo=5000
def factorial(n):
    a=1
    if n<=1:
        return 1
    else:
        for i in range(2, n+1):
            a*=i
    return a

def chudnovskyBig(n): #http://en.wikipedia.org/wiki/Chudnovsky_algorithm
    pi = Decimal(0)
    k = 0
    while k < n:
        pi += (Decimal(-1)**k)*(Decimal(factorial(6*k))/((factorial(k)**3)*(factorial(3*k)))* (13591409+545140134*k)/(640320**(3*k)))
        k += 1
        if k%5==0:
            print 'Cycle ',k,' completed'
    pi = pi * Decimal(10005).sqrt()/4270934400
    pi = pi**(-1)
    return pi


getcontext().prec = countUpTo
print 'Must go up to ', (countUpTo/14)+(14*3), ' cycles'
pi=chudnovskyBig((countUpTo/14)+(14*3))
print "Length: ", getcontext().prec, ", ", pi