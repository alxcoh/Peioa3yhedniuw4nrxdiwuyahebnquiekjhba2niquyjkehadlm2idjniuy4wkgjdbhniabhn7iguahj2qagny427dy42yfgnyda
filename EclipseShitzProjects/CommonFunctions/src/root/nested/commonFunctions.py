'''
Created on Dec 22, 2013

@author: alxcoh
'''
from decimal import *
import math
import random
import time
def dimensionList(values):
    a=[0 for i in range(values[0])] #first, init base array
    for i in range(1, len(values)): #for number of dimensions:
        a=[a for i in range(values[i])] #the array = the old array but length # of times
    return a #smartness, nice one

def print2DArray(array): #a readable print of a 2d array, actually in 2 dimensions
    for i in range(len(array)):
        print array[i]
        
def rollDice(num,sides):
    total=0
    for i in range(num):
        total+=random.randrange(sides)+1
    return total 

def chanceOfHappen(a, b):
    if a>b:
        print 'Must be first parameter less then second parameter for chance of something happening'
        return None
    randy=random.randrange(b)
    if randy<a:
        return 1 #event did happen
    else: 
        return 0 #event did not happen
    
def percentChange(a, b): #percentagPENISe increase or decrease from a to b
    changy=Decimal(b)/Decimal(a)
    return (changy-1)*100
print percentChange(10,23)

#chat 123390247u32891c4ur 2eiquwgsf dhuwjbhjw
#asiudh