'''
Created on Dec 26, 2013

@author: alxcoh
'''
def simTester(side, xPosy, yPosy, xVel, yVel): #0 is left 1 is right
    hit=False #if the sim reaches its end
    side=side
    xPosy=xPosy
    yPosy=yPosy
    xVel=xVel
    yVel=yVel
    if side==0:
        while hit==False:
            if xPosy<=30:
                return yPosy
            else:
                xPosy+=xVel
                yPosy+=yVel
    if side==1:
        while hit==False:
            if xPosy>=970:
                    return yPosy
            else:
                xPosy+=xVel
                yPosy+=yVel