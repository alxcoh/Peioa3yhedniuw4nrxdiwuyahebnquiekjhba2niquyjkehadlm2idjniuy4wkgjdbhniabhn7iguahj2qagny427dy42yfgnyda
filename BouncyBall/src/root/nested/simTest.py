'''
Created on Dec 26, 2013

@author: alxcoh
'''
def simTester(side, xPosy, yPosy, xVel, yVel): #0 is left 1 is right, DASCH IST ALEXS FUNCTION
    #btw this is long and unnecessary look at mine
    hit=False #if the sim reaches its end
    side=side
    xPosy=xPosy
    yPosy=yPosy
    xVel=xVel
    yVel=yVel
    '''
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
    '''
    if side==False:
        while hit==False:
            
            if yPosy>=660:
                yVel=-yVel
                yPosy=650
                
            if yPosy<=40:
                yVel=-yVel
                yPosy=50

            if xPosy<=60:
                xVel=-xVel
                xPosy=80
                
            xPosy+=xVel
            yPosy+=yVel
            
            if xPosy>=940:
                hit=True
                print 'Expexted: ', yPosy
                return yPosy            

def FORESEETHEFUTURE (side, x, y, Vx, Vy, sizeX, sizeY, paddleSize): #false is left, true is right
    '''more natural to me because physics
       sizeX should be between ball's end and paddle
       sizeY should be total size up/down
       remember to account for paddlesize
       returns y position wanted
    '''
    firstFramesToYWall=0 #time from paddle to first wall
    wavelength=0 #from wall back to wall
    if Vy==0: return y #obvious
    if Vy>0: firstFramesToYWall=(sizeY-y)/Vy
    if Vy<0: firstFramesToYWall=-y/Vy
    newX=Vx*firstFramesToYWall+x
    wavelength=2*sizeY/Vy*Vx
    n=0
    while not side and newX+n*wavelength>70:
        n+=1
        print 'while not loop done: iter'
    
    while side and not newX+n*wavelength<930:
        n+=1
        print 'while not loop done: iter'
    distFromPaddle=0
    if side:
        distFromPaddle=newX+n*wavelength+70
        if Vy>0:
            return sizeY-abs(distFromPaddle/Vx*Vy)
        if Vy<0:
            return abs(distFromPaddle/Vx*Vy)
    if side: 
        distFromPaddle=newX+n*wavelength-70
        if Vy>0:
            return sizeY-abs(distFromPaddle/Vx*Vy)
        if Vy<0:
            return abs(distFromPaddle/Vx*Vy)