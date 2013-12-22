'''
Created on Dec 22, 2013

@author: alxcoh
'''
from decimal import *
import random
import time
import math
#poop
def dimensionList(values):
    a=[0 for i in range(values[0])] #first, init base array
    for i in range(1, len(values)): #for number of dimensions:
        a=[a for i in range(values[i])] #the array = the old array but length # of times
    return a #smartness, nice one

def print2DArray(array): #a readable print of a 2d array, actually in 2 dimensions
    for i in range(len(array)):
        print array[i]
        
def chanceOfHappen(a, b):
    if a>b:
        print 'Must be frst parameter less then second parameter for chance of something happening'
        return None
    randy=random.randrange(b)
    if randy<a:
        return 1 #event did happen
    else: 
        return 0 #event did not happen