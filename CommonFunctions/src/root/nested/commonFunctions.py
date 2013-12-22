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
#pooo