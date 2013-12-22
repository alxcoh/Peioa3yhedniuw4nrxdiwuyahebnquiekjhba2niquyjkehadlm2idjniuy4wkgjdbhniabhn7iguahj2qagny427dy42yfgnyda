def gcd(x, y):
    if x>y:
        a=x
        b=y
    elif y>x:
        a=y
        b=x
    elif x==y:
        return x
    c=a
    d=b
    notFound=1
    while notFound==1:
        if(c%d==0):
            return d
            notFound=0
            break
        else:
            e=c
            c=d
            d=e%d