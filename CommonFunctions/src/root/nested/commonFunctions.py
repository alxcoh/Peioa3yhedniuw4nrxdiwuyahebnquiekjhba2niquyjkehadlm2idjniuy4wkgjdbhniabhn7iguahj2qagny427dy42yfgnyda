'''
Created on Dec 22, 2013

@author: alxcoh
'''

def dimensionList(values):
    a=[0 for i in range(values[0])]
    for i in range(1, len(values)):
        a=[a for i in range(values[i])]
    return a