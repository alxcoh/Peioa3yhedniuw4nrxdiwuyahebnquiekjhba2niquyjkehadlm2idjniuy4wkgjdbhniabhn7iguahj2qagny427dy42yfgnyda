def phi(a, b):
    return (a-1)*(b-1)
def ExtEucAlg(y, x):
    #a is the mod, b is the this we want to find the inverse of 
    p=[i for i in range(3)]
    q=[1 for i in range(3)]
    a=x
    b=y
    notFound=1
    numOn=0
    while notFound==1:
        print '*********************\n'
        print 'a=', a, '\n'
        print 'b=', b, '\n'
        print 'p[0]=', p[0], '\n'
        print 'p[1]=', p[1], '\n'
        print 'p[2]=', p[2], '\n'
        print 'q[0]=', q[0], '\n'
        print 'q[1]=', q[1], '\n'
        print 'q[2]=', q[2], '\n'
        if a%b==0:
            return (p[1]-p[2]*q[1])%x
            notFound=0
            break
        c=a%b
        a=b
        b=c
        if numOn>=2:
            p[0]=p[1]
            p[1]=p[2]
        q[0]=q[1]
        q[1]=q[2]
        p[2]=(p[0]-p[1]*q[0])%x
        q[2]=int(a/b)
        numOn+=1


