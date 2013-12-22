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
<<<<<<< HEAD
#pooo
=======

def chanceOfHappen(a, b):
    if a>b:
        print 'Must be frst parameter less then second parameter for chance of something happening'
        return None
    randy=random.randrange(b)
    if randy<a:
        return 1 #event did happen
    else: 
        return 0 #event did not happen
<<<<<<< HEAD
    
def percentIncrease(a, b): #percentage increase or decrease from a to b
    changy=Decimal(b/a)
    return 1-changy

print percentIncrease(1, 2)
=======
>>>>>>> e2d60e5268476637dd32f037cc65905c845d8ab6
>>>>>>> 4d8678244d13fea0df85561ee6cb6fa137f9d18a
