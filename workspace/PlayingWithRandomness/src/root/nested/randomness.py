
start=pow(2, 1024)
def primeCheck(n):
    for i in range (2, 60, 13):
        if pow(i, n-1, n)==1:
            return 1
            break
    else:
        return 0
for x in range(start+1, 2*start-1, 2):
        if primeCheck(x)==1:
            print x, '\n'

