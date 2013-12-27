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
yPos=400.0
xPos=450.0
maxDown=10.0
maxRight=50.0
startspeedD=8
startspeedR=8
goingDown=8.0
goingRight=8.0
W=False
S=False
UP=False
DOWN=False
randomness=4 #if you actually want to play crazyball, set this at 4-6 for regular, 6-10 is madness, 10-20 for insanity
crazyDelay=5 #how often velocity changes in crazyball
FPS=60
fpsClock=pygame.time.Clock()
paddleHeight=[150 for i in range(2)]

paddleY=[350-(paddleHeight[0]/2), 350-(paddleHeight[1]/2)] # 0 is left, 1 is right

paddleSpeed=[10,3]

paddleLeft=pygame.Rect(15, paddleY[0], 15, paddleHeight[0])
paddleRight=pygame.Rect(970, paddleY[1], 15, paddleHeight[1])


def paddleTouched():
    if xPos>=940 and yPos>=paddleY[1]-30 and yPos<=paddleY[1]+paddleHeight[1]+30: 
        return 1
    if xPos<=60 and yPos>=paddleY[0]-30 and yPos<=paddleY[0]+paddleHeight[0]+30:
        return 2
    return 0    
        
def CPUTIME(value):
    if paddleY[1]+75>value:
        #print 'goingUp'
        paddleY[1]-=paddleSpeed[1]
    elif paddleY[1]+75<value:
        #print 'goingDown'
        paddleY[1]+=paddleSpeed[1]
def randomizeMovement(mvt, rand):
    return mvt + random.randrange(rand)

def ballCheck(a, b, c, d):
    global goingDown
    global goingRight
    global xPos
    global yPos
    global randomness
    global scoreL
    global scoreR
    global pause
    goingDown=a
    goingRight=b
    xPos=c
    yPos=d
    if yPos>=660 or yPos<=40:
        goingDown=-goingDown
        if yPos>=660:
            yPos=650
        else:
            yPos=50

    paddleTouchedVal=paddleTouched() #0 is not touched, 1 is right touched, 0 is left touched
    if paddleTouchedVal==1 or paddleTouchedVal==2:
        goingRight=-goingRight
        if goingRight>=0:
            goingRight+=random.randrange(0, 3)
        elif goingRight<0:
            goingRight-=random.randrange(0, 3)
        goingDown+=random.randint(-randomness, randomness)

        global val
        val=simTester(False, xPos, yPos, goingRight, goingDown)
        if xPos>=930:
            xPos=920
        if xPos<=70:
            xPos=80
    if xPos>=970:
        scoreL+=1
        xPos=450
        yPos=400
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
            
        val=simTester(False, xPos, yPos, goingRight, goingDown)
        pause=True
    if xPos<=30:
        xPos=450
        yPos=400
        '''goingRight=randomizeMovement(0,startspeedR*1.5)
        goingDown=randomizeMovement(0,startspeedD*1.5) 
        while not (goingRight<-startspeedR/2 or goingRight>startspeedR/2) and not (goingDown<-startspeedD/2 or goingDown>startspeedD/2):
            goingRight=randomizeMovement(0,22)-11
            goingDown=randomizeMovement(0,22)-11'''
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
        scoreR+=1
        val=simTester(False, xPos, yPos, goingRight, goingDown)
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
        background.fill(GREEN.FORESTGREEN.full)
        myBallCenterPos = (int(xPos+0.5), int(yPos+0.5)) #normally casting to int goes to next lowest int, adding 0.5 makes behavior like a round
        pygame.draw.circle(background, BLACK.full, myBallCenterPos, 30)
        pygame.draw.rect(background, BLUE.AZURE.full, paddleLeft)
        pygame.draw.rect(background, BLUE.AZURE.full, paddleRight)
        goingDown, goingRight = ballCheck(goingDown, goingRight, xPos, yPos)
        xPos, yPos = ballMove(goingDown, goingRight, xPos, yPos)
        paddleLeft.top=paddleY[0]
        paddleRight.top=paddleY[1]
        #elif CPU2: CPUTIME(True)
        
    else: # paused
        
        screen.blit(s, (0,0))    # (0,0) are the top-left coordinates
        screen.blit(pauseText, textpos) # use screen.blit to print to front apparently
    # ALL DA TIME
    
    screen.blit(regularFont.render(str(scoreL), 0, BLUE.ROYALBLUE.full),(50,50))
    screen.blit(regularFont.render(str(scoreR), 0, BLUE.ROYALBLUE.full),(923,50))
    pygame.display.flip()
    pygame.display.update()
    if CPU1: CPUTIME(val)    
    
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


'''
###############################################################################
