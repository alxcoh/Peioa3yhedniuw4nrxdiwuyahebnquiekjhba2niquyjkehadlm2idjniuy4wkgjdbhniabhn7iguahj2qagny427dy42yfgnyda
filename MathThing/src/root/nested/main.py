import random
import decimal
from decimal import *
class Character:
    def __init__(self, ordNum, prob):
        self.ordNum=ordNum
        self.prob=prob
        self.state=1 #1 is alive 0 is dead
    
    def shoot(self, a): #a is who is being shot
        randy=random.randrange(self.prob)
        if randy==0:
            #print 'shot connected from', self.ordNum
            a.state=0
            #print a.ordNum, ' is dead'
            return 1 #person killed
        else:
            #print 'shot missed from', self.ordNum
            return 0 #person alive
       
    def logicA1(self, b, c):
        if b.state==1 and c.state==1:
            return None
        elif b.state==0 and c.state==0:
            return 10 #game over charA wins
        elif b.state==0:
            if self.shoot(c)==1:
                return c.ordNum
        elif c.state==0:
            if self.shoot(b)==1:
                return b.ordNum
       
        return 100
    
    def logicA2(self, b, c):
        if (b.state==1 and c.state==1) or (b.state==0 and c.state==1):
            if self.shoot(c)==1:
                return c.ordNum
        elif b.state==1 and c.state==0:
            if self.shoot(b)==1:
                return b.ordNum
        elif b.state==0 and c.state==0:
            return 10
            
        return 100
    
    def logicA3(self, b, c):
        if (b.state==1 and c.state==1) or (b.state==1 and c.state==0):
            if self.shoot(b)==1:
                return b.ordNum
        elif c.state==1 and b.state==0:
            if self.shoot(c)==1:
                return c.ordNum
        elif b.state==0 and c.state==0:
            return 10
        
        return 100

    def logicA4(self, b, c):
        if b.state==1 and c.state==1:
            randy=random.randrange(3)
            if randy==0:
                return None
            if randy==1:
                if self.shoot(b)==1:
                    return b.ordNum
            if randy==2:
                if self.shoot(c)==1:
                    return c.ordNum
        elif b.state==0 and c.state==0:
            return 10
        
        elif b.state==1 and c.state==0:
            if self.shoot(b)==1:
                return b.ordNum
            
        elif b.state==0 and c.state==1:
            if self.shoot(c)==1:
                return c.ordNum
    
    def logicA5(self, b, c):
        if b.state==1 and c.state==1:
            randy=random.randrange(2)
            if randy==0:
                if self.shoot(b)==1:
                    return b.ordNum
            if randy==1:
                if self.shoot(c)==1:
                    return c.ordNum
        elif b.state==0 and c.state==0:
            return 10
        
        elif b.state==1 and c.state==0:
            if self.shoot(b)==1:
                return b.ordNum
            
        elif b.state==0 and c.state==1:
            if self.shoot(c)==1:
                return c.ordNum
        
        return None
    def turn(self, b, c, f):
        if self.ordNum==0:
            if f==0:
                return charA.logicA1(b, c)
            elif f==1:
                return charA.logicA2(b, c)
            elif f==2:
                return charA.logicA3(b, c)
            elif f==3:
                return charA.logicA4(b, c)
            elif f==4:
                return charA.logicA5(b, c)
        elif self.ordNum==1 or self.ordNum==2:
            if c.state==1:
                if self.shoot(c)==1:
                    return c.ordNum
            elif c.state==0 and b.state==0:
                return self.ordNum+10 #a won

            elif c.state==0 and b.state==1:
                if self.shoot(b)==1:
                    return b.ordNum
        else: return 100
charA=Character(0, 3)
charB=Character(1, 2)
charC=Character(2, 1)
aCount=0
bCount=0
cCount=0

gameOn=1

county=0;

def itr(a): #0 is good logic 1 is bad logic
    resA=100
    resB=100
    resC=100
    '''print 'start'
    print charA.state
    print charB.state
    print charC.state'''
    
    if charA.state==1:
        returny=0
        #print 'a turn'
        resA=charA.turn(charB, charC, a)
        if resA==10:
            #print "Player A wins"
            returny=1
            return 0, 0
    if charB.state==1:
        #print 'b turn'
        resB=charB.turn(charA, charC, a)
        if resB==11:
            #print "Player B wins"
            returny=1
            return 0, 1
    if charC.state==1:
        #print 'c turn'
        resC=charC.turn(charA, charB, a)
        if resC==12:
            #print "Player C wins"
            returny=1
            return 0, 2
        
    if returny==0: return 1, 100
cycleTimes=500000
logicNum=5
aCount=[0 for i in range(logicNum)]
bCount=[0 for i in range(logicNum)]
cCount=[0 for i in range(logicNum)]
#print '\nStarting Bad Logic cycle:'
for x in range(logicNum):
    print '\nStarting cycle for logic ', x+1
    for i in range(cycleTimes):
        gameOn=1
        charA.state=1
        charB.state=1
        charC.state=1
        while gameOn==1:
            res=0
            addr=0
            try:
                res, addr=itr(x)
            except TypeError:
                print 'exception'
                res=0
                addr=100
                
            gameOn=res
            if addr==100:
                continue
            if addr==0:
                aCount[x]+=1
                county+=1
            if addr==1:
                bCount[x]+=1
                county+=1
            if addr==2:
                cCount[x]+=1
                county+=1
            if county%10000==0:
                print county
    
    gameCount=1
    county=0


for x  in range(logicNum):
    print '\nFor logic ', x+1, ':'
    print '\nA won ',aCount[x], ' times, ', Decimal(aCount[x]*100)/Decimal(cycleTimes), '% of the time'
    print '\nB won ',bCount[x], ' times, ', Decimal(bCount[x]*100)/Decimal(cycleTimes), '% of the time'
    print '\nC won ',cCount[x], ' times, ', Decimal(cCount[x]*100)/Decimal(cycleTimes), '% of the time'
    
aCounter=[0 for i in range(logicNum)]

for x  in range(1, logicNum):
    aCounter[x]=Decimal(aCount[x]*100)/Decimal(cycleTimes)
    print '\nDiffernce in percent won between good strategy and strategy ', x+1, ': ', Decimal(aCount[0]*100)/Decimal(cycleTimes)-aCounter[x], '%'
    percentIncrease=100*((Decimal(aCount[0])/Decimal(aCount[x]))-1)
    print 'Advantage good strategy gives over strategy ', x+1, ': ', percentIncrease, '%'
#random message
#poooo
