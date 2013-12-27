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
    if yVel>=0:
        goingDown=True
    else:
        goingDown=False
    if side==False:
        while hit==False:
            if xPosy>=970:
                hit=True
                print yPosy+75
                return yPosy+75
            else:
                if goingDown==True:
                    yPosy+=yVel
                elif goingDown==False:
                    yPosy-=yVel
                if yPosy>670:
                    goingDown=False
                elif yPosy<30:
                    goingDown=True
                xPosy+=xVel
                                