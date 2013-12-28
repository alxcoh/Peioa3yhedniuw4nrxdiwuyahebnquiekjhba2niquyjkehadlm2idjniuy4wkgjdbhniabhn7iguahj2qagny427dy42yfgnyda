'''
Created on Dec 23, 2013

@author: alxcoh and 71619997a
'''

from commonPygame import *
from simTest import *

#Colors
scoreL=0
scoreR=0
pause=False
end=False
crazyball=False #  :D
CPU1=True
CPU2=False
loopnum=1
yPos=350.0
xPos=500.0
maxDown=50.0
maxRight=50.0
startspeedD=8
startspeedR=8
goingDown=8.0
goingRight=8.0
maxDown=15
maxRight=50
startspeedD=8
startspeedR=8
goingDown=startspeedD
goingRight=startspeedR
W=False
S=False
UP=False
DOWN=False
randomness=3 #if you actually want to play crazyball, set this at 4-6 for regular, 6-10 is madness, 10-20 for insanity
crazyDelay=5 #how often velocity changes in crazyball
FPS=60
fpsClock=pygame.time.Clock()
paddleHeight=[200, 150]

paddleY=[350-(paddleHeight[0]/2), 350-(paddleHeight[1]/2)] # 0 is left, 1 is right

paddleSpeed=[10, 2.5]

paddleLeft=pygame.Rect(15, paddleY[0], 15, paddleHeight[0])
paddleRight=pygame.Rect(970, paddleY[1], 15, paddleHeight[1])


def paddleTouched():
    if xPos>=940 and yPos>=paddleY[1]-30 and yPos<=paddleY[1]+paddleHeight[1]+30:
        #print yPos 
        return 1
    if xPos<=60 and yPos>=paddleY[0]-30 and yPos<=paddleY[0]+paddleHeight[0]+30:
        return 2
    return 0    
        
def CPUTIME(value, howMany): #tru is both, false is just right
    if paddleY[1]+(paddleHeight[1]/2)>value:
        #print 'goingUp'
        paddleY[1]-=paddleSpeed[1]
    elif paddleY[1]+(paddleHeight[1]/2)<value:
        #print 'goingDown'
        paddleY[1]+=paddleSpeed[1]
        
    if howMany:
        if paddleY[0]+(paddleHeight[0]/2)>yPos:
            paddleY[0]-=paddleSpeed[0]
        
        if paddleY[0]+(paddleHeight[0]/2)<yPos:
            paddleY[0]+=paddleSpeed[0]
        
def randomizeMovement(mvt, rand):
    return mvt + random.randrange(0, rand)

def ballCheck(a, b, c, d):
    global goingDown
    global goingRight
    global xPos
    global yPos
    global randomness
    global scoreL
    global scoreR
    global pause
    global val
    global passed
    passed=False
    global passy
    passy=False
    goingDown=a
    goingRight=b
    xPos=c
    yPos=d
    if yPos>=660 or yPos<=40:
        goingDown=-goingDown
        if yPos>=660:
            #print 'BOUNCE BOT:', xPos, yPos, goingRight, goingDown
            yPos=650
        else:
            #print 'BOUNCE TOP:', xPos, yPos, goingRight, goingDown
            yPos=50

    paddleTouchedVal=paddleTouched() #0 is not touched, 1 is right touched, 2 is left touched
    if paddleTouchedVal==1 or paddleTouchedVal==2:
        if paddleTouchedVal==1:
            '''
            print 'Expected: ', val
            print 'Real: ', yPos, goingRight, goingDown
            print 'Difference: ', val-yPos
            '''
            pass
        
        goingRight=-goingRight
        randVal=random.randrange(0, randomness+1)
        if goingRight>=0:
            goingRight+=randVal
        elif goingRight<0:
            goingRight-=randVal
        if goingDown>=0:
            goingDown+=randVal
        elif goingDown<0:
            goingDown-=randVal 
        
        goingDown+=random.randint(-randomness, randomness+1)

        passy=False
        
        if xPos>=930:
            xPos=920
        if xPos<=70:
            xPos=80
        
        if CPU1==True: val=simTester(False, xPos, yPos, goingRight, goingDown)
        #val=FORESEETHEFUTURE(False,xPos,yPos,goingRight,goingDown,900,720,0)
    
    if (goingRight<0 and xPos<500) or (goingRight>0 and xPos>500) and not passy:
        passed=True
        
    if passed==True:
        val=simTester(False, xPos, yPos, goingRight, goingDown)
        passed=False
        passy=True
    
    if xPos>=970: 
        print 'Expected: ', val
        print 'Real: ', yPos, goingRight, goingDown
        print 'Difference: ', val-yPos
        scoreL+=1
        xPos=500
        yPos=350
        paddleY[1]=275
        paddleY[0]=275
        '''
        goingRight=randomizeMovement(0,startspeedR*1.5)
        goingDown=randomizeMovement(0,startspeedD*1.5) 
        while not (goingRight<-startspeedR/2 or goingRight>startspeedR/2) and not (goingDown<-startspeedD/2 or goingDown>startspeedD/2):
            goingRight=randomizeMovement(0,startspeedR*1.5)
            goingDown=randomizeMovement(0,startspeedD*0.7) #alex this is much much better than your code b/c it takes the origi
        #thefuck is an origi this doesnt work
        '''  
        rVal=random.randrange(-2, 2)
        dVal=random.randrange(-2, 2)
        if rVal<0:
            goingRight=rVal-4
        elif rVal>=0:
            goingRight=rVal+4
            
        if dVal<0:
            goingDown=dVal-4
        elif dVal>=0:
            goingDown=dVal+4

        
        if CPU1==True: val=simTester(False, xPos, yPos, goingRight, goingDown)
        
        pause=True
        
    if xPos<=30:
        scoreR+=1
        xPos=500
        yPos=350
        paddleY[0]=275
        paddleY[1]=275
        '''
        goingRight=randomizeMovement(0,startspeedR*1.5)
        goingDown=randomizeMovement(0,startspeedD*1.5) 
        while not (goingRight<-startspeedR/2 or goingRight>startspeedR/2) and not (goingDown<-startspeedD/2 or goingDown>startspeedD/2):
            goingRight=randomizeMovement(0,startspeedR*1.5)
            goingDown=randomizeMovement(0,startspeedD*0.7) #alex this is much much better than your code b/c it takes the original speed into consideration
        '''
        rVal=random.randrange(-2, 2)
        dVal=random.randrange(-2, 2)
        if rVal<0:
            goingRight=rVal-4
        elif rVal>=0:
            goingRight=rVal+4
            
        if dVal<0:
            goingDown=dVal-4
        elif dVal>=0:
            goingDown=dVal+4

        
        if CPU1==True: val=simTester(False, xPos, yPos, goingRight, goingDown)
        
        pause=True
        
    return goingDown, goingRight

def ballMove(a, b, c, d):
    global goingDown
    global goingRight
    global xPos
    global yPos
    global randomness
    goingDown=a
    goingRight=b
    xPos=c
    yPos=d
    if crazyball and loopnum % crazyDelay==0:
        goingRight=randomizeMovement(goingRight,randomness) #randomize every 5 frames for crazyball
        goingDown=randomizeMovement(goingDown,randomness)

    while goingRight==0:
        goingRight=randomizeMovement(goingRight,2) # this and
    while goingDown==0:
        goingDown=randomizeMovement(goingDown,2) # this are to prevent stalling

    xPos+=goingRight
    yPos+=goingDown
    return xPos, yPos

regularFont = pygame.font.Font(None,60)
bigFont = pygame.font.Font(None, 240)

pauseText = bigFont.render("Paused", 0, BLUE.ROYALBLUE.full) # use .col() to get the actual color itself
textpos = pauseText.get_rect()
textpos.centerx = background.get_rect().centerx
textpos.centery = background.get_rect().centery
s = pygame.Surface((1000,750))  # the size of your rect
s.set_alpha(2)                # alpha level
s.fill((255,255,255))           # this fills the entire surface

val=simTester(False, xPos, yPos, goingRight, goingDown)
while not end:
    global val
    if not pause: # ingame
        if goingDown>maxDown:
            goingDown=maxDown
        if goingDown<-maxDown:
            goingDown=-maxDown
        if goingRight>maxRight:
            goingRight=maxRight
        if goingRight<-maxRight:
            goingRight=-maxRight
        loopnum+=1
        screen.blit(background, (0, 0))
        background.fill(BLUE.TEAL.full)
        myBallCenterPos = (int(xPos+0.5), int(yPos+0.5)) #normally casting to int goes to next lowest int, adding 0.5 makes behavior like a roun
        goingDown, goingRight = ballCheck(goingDown, goingRight, xPos, yPos)
        xPos, yPos = ballMove(goingDown, goingRight, xPos, yPos)
        paddleLeft.top=paddleY[0]
        paddleRight.top=paddleY[1]
        #pygame.draw.circle(background, BLACK.full, myBallCenterPos, 30)
        concentricCircle(background, [BLACK.full, RED.FUCHSIA.full], myBallCenterPos, [30, 15])
        pygame.draw.rect(background, YELLOW.GOLDENROD.full, paddleLeft)
        pygame.draw.rect(background, YELLOW.GOLDENROD.full, paddleRight)
        if CPU1: 
            if not CPU2:
                CPUTIME(val, False)
            
            if CPU2:
                CPUTIME(val, True)
        
        
    else: # paused
        
        screen.blit(s, (0,0))    # (0,0) are the top-left coordinates
        screen.blit(pauseText, textpos) # use screen.blit to print to front apparently
    # ALL DA TIME
    
    screen.blit(regularFont.render(str(scoreL), 0, BLACK.full),(50,50))
    screen.blit(regularFont.render(str(scoreR), 0, BLACK.full),(923,50))
    pygame.display.flip()
    pygame.display.update()
    
    
    for event in pygame.event.get():
        if event.type == QUIT:
            end=True
            break
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                end=True
                pygame.quit()
                break
            if event.key == K_p: 
                pause=not pause     # pause or unpause
            if event.key==K_w:
                W=True
            if event.key==K_s:
                S=True
            if event.key==K_UP:
                UP=True
            if event.key==K_DOWN:
                DOWN=True
        if event.type==KEYUP:
            if event.key==K_w:
                W=False
            if event.key==K_s:
                S=False
            if event.key==K_UP:
                UP=False
            if event.key==K_DOWN:
                DOWN=False
    if not pause:
        if not CPU2:
            if W:
                paddleY[0]-=paddleSpeed[0]
                if paddleY[0]<0: paddleY[0]=0
            if S:
                paddleY[0]+=paddleSpeed[0]
                if paddleY[0]+paddleHeight[0]>700: paddleY[0]=700-paddleHeight[0]
        if not (CPU1 or CPU2):
            if UP:
                paddleY[1]-=paddleSpeed[1]
                if paddleY[1]<0: paddleY[1]=0
            if DOWN:
                paddleY[1]+=paddleSpeed[1]
                if paddleY[1]+paddleHeight[1]>700: paddleY[1]=700-paddleHeight[1]
        
    fpsClock.tick(FPS)

################################### C H A T ###################################
'''
say your name then a colon, then message
ALEX: I have an idea to eliminate processing power. We can modify it so it does a certain constant amount of
      iterations through the prediction each frame after it hits a paddle, but it does not finish in one. 
      (It may, for instance, calculate 10 frames in advance every frame, but every time work with the same data
      that it got once it hit the paddle, it just progresses in the simulation using the same data as the frames
    are progressing)
GABRIEL: Your shit's fucked with fast speeds. I beat it 10-6 and the computer (doing simplest ai) beat it 10-3.
         You probably didn't account for the ball's radius or something. Also, I fixed the points because you
         couldn't score on one side, but occasionally it throws me     
             values[counter][0]=xPosy
         IndexError: list index out of range
         so yeah, fix your shit
'''
###############################################################################
