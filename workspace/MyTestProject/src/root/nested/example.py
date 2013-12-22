'''
Created on Nov 28, 2013

@author: alxcoh
'''
#THIS IS A PROGRAM TO GENERATE A CERTAIN LENGTH RSA KEY. RSA KEYS ARE THE PRODUCTS OF TWO LARGE PRIMES

'''
FUNCTIONALITY TO ADD: 
-OPTION OF MAKING A KEY/ENCRYPTING/DECRYPTING/SIGNING 
-REPLACE CURRENT PRNG WITH A CSPRNG
-GIVE IT OAEP OR SOME OTHER GOOD PADDING
'''

#variables
import random
accuracy=15#accuracy is 2^-accuracy probability that it is a faux prime
keyLen=1012 #length of the full key
while True:
    keyLen=int(raw_input("\nEnter key length: "))
    if keyLen<256:
        print '\nLength must be greater than or equal to 256. Choose again.'
    elif keyLen%2==1:
        print '\nNumber must be even. Choose again.'
    else:
        break
while True:
    accuracy=int(raw_input("\nEnter the accuracy: "))
    if accuracy<1:
        print '\nAccuracy must be a natural number'
    else:
        break
bitKey=keyLen/2 #length of each prime multiplied to get full key
primeNums = [0 for i in range(2)]
start=pow(2, bitKey)
notDone=1
numbers=[0 for i in range(2)]
d=1
e=65537
lenPerChar=2
substitutionLen=28
extraneous=1
finding=1
print '\nMaximum characters in message for key =', len(str(2**keyLen))/2, ' characters.\n'
while True:
    message=raw_input("Enter a message: ")
    if (ord(message[0])<38 or ord(message[0])==43) and ord(message[0])!=34:
        print '\nPlease choose a different starting character\n'
    elif len(message)>=len(str(2**keyLen))/2:
        print '\nLength of message: ', len(message)
        print 'Max length: ', len(str(2**keyLen))/2
        print '\nMessage too long, enter new message'
    else:
        break
#functions
def padMessage(n):
    plaintext=str(n)
    padded=[" " for i in plaintext]
    for i in range(len(plaintext)):
        extraneous=1
        if ord(plaintext[i])-substitutionLen==6:
            padded[i]='15'
        if ord(plaintext[i])-substitutionLen==15:
            padded[i]='06'
        elif ord(plaintext[i])-substitutionLen>10 and ord(plaintext[i])-substitutionLen<100 and ord(plaintext[i])-substitutionLen!=15:
            padded[i]=str(ord(plaintext[i])-substitutionLen)#so everything is 2 digits
        elif ord(plaintext[i])-substitutionLen<10 and ord(plaintext[i])-substitutionLen>0 and ord(plaintext[i])-substitutionLen!=6:
            padded[i]=str('0')+str(ord(plaintext[i])-substitutionLen)
        elif ord(plaintext[i])-substitutionLen<=0 or ord(plaintext[i])-substitutionLen>=100:
            print '\nExtranious characters used. Will convert all extraneous characters to \'~\' \n'
            extraneous=0
            print 
            padded[i]=str(ord('~')-substitutionLen)
    paddedMessage=0
    for i in range(len(plaintext)):
        paddedMessage=int(str(paddedMessage)+padded[i])
    return paddedMessage, extraneous
def dePad(n):
    paddedMessage=n
    a=len(str(paddedMessage))
    b=str(paddedMessage)
    padded=['' for i in range(a/lenPerChar)]
    for i in range(a/lenPerChar):
        padded[i]=b[lenPerChar*i]+b[lenPerChar*i+1]#+b[lenPerChar*i+2]
        if b[lenPerChar*i]+b[lenPerChar*i+1]=='06':
            padded[i]='15'
        if b[lenPerChar*i]+b[lenPerChar*i+1]=='15':
            padded[i]='06'
    for i in range(len(padded)):
        padded[i]=chr(int(padded[i])+substitutionLen)
    plaintext=''.join(padded)
    return plaintext

def phi(a, b):
    return (a-1)*(b-1)

def egcd(a, b):
    x=0
    y=1
    u=1
    v=0
    while a != 0:
        q = b//a
        r = b%a
        m = x-u*q
        n = y-v*q
        b = a
        a = r
        x = u
        y = v
        u = m
        v = n
    return b, x, y

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

def genRand():
    return random.randrange(start+1, 2*start-1 , 2) #finds a random odd number that is exactly half the amount of bits as the final key
def primeCheck(n):
    for i in range (2, 13*(accuracy-1)+3, 13): #chooses the base to check with by going up by 13 from 2 up to 13*accuracy
        if pow(i, n-1, n)!=1: #fermat test here
            returner=0
            break  
    else:
        returner=1
    return returner

#finding the primes
for x in range(2): #finds 2 random primes instead of 1
    notDone=1
    startNum=genRand()
    while notDone==1: #finds the closest prime to the random number generated
        if primeCheck(startNum)==1:
            print '\nPrime ', x+1, ': ', startNum
            numbers[x]=startNum
            notDone=0
            break
        else:
            startNum+=2

#calculations and setting stuff      
n=numbers[0]*numbers[1]
phiNums=phi(numbers[0], numbers[1])
d=modinv(e, phiNums)
paddedMessage, extraneous=padMessage(message)
c=pow(paddedMessage, e, n)
m=pow(c, d, n) #deciphered padded
mnP=dePad(m) #message not padded
#checking for message too big


#printing everything out
print '\nFinal key: ', n #shows the final keyLen length key
print '\nPhinums=', phiNums
print '\nSecret key: ', d, 
print '\n\nThe message is: ', message,
print '\n\nPlaintext padded: ', paddedMessage,
print '\n\nCiphertext: ', c,
print '\n\nMessage decrypt padded: ', m
if extraneous==1:
    print '\nMessage Decrypted: ', mnP
if extraneous==0:
    print "\nMessage Decrypted (there where extranious characters, and they were replaced with a '~'): ", mnP
mnP=dePad(m) #message not padded