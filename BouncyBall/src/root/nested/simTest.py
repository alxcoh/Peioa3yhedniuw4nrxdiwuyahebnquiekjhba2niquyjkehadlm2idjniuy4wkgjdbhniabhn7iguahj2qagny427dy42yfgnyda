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
        startY=True
    elif yVel<0:
        goingDown=False
        startY=False
    if xVel>=0:
        goingRight=True
        start=True
    else:
        goingRight=False
        start=False
    if side==False:
        while hit==False:
            if xPosy>=970:
                hit=True
                print 'I expect: ', yPosy
                return yPosy
            else:
                if yPosy>670:
                    goingDown=False
                elif yPosy<30:
                    goingDown=True
                 
                if xPosy<=60:
                    goingRight=True    
                
                if goingDown==True:
                    if startY==True:
                        yPosy+=yVel
                    if startY==False:
                        yPosy-=yVel
                elif goingDown==False:
                    if startY==True:
                        yPosy-=yVel
                    if startY==False:
                        yPosy+=yVel
                    
                if goingRight==True:
                    if start==True:
                        xPosy+=xVel
                    elif start==False:
                        xPosy-=xVel
                
                elif goingRight==False:
                    if start==True:
                        xPosy-=xVel
                    elif start==False:
                        xPosy+=xVel
                                