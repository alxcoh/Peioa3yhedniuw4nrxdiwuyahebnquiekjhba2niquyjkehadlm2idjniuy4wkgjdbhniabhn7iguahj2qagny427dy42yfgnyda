'''
Created on Dec 23, 2013

@author: alxcoh and 71619997a
'''

from commonPygame import *


#Colors
scoreL=0
scoreR=0
pause=False
end=False
crazyball=False #  :D
loopnum=1
yPos=400.0
xPos=450.0
maxDown=15.0
maxRight=15.0
goingDown=8.0
goingRight=8.0
randomness=2 #if you actually want to play crazyball, set this at 4-6 for regular, 6-10 is madness, 10-20 for insanity
crazyDelay=5 #how often velocity changes in crazyball
paddleHeight=[150 for i in range(2)]

paddleY=[350-(paddleHeight[0]/2), 350-(paddleHeight[1]/2)] # 0 is left, 1 is right

paddleSpeed=[10 for i in range(2)]

paddleLeft=pygame.Rect(30, paddleY[0], 15, paddleHeight[0])
paddleRight=pygame.Rect(970, paddleY[1], 15, paddleHeight[1])


def paddleTouched():
    if xPos>=930 and yPos>=paddleY[1] and yPos<=paddleY[1]+paddleHeight[1]: 
        return True
    if xPos<=70 and yPos>=paddleY[0] and yPos<=paddleY[0]+paddleHeight[0]:
        return True
    return False    
        
def randomizeMovement(mvt, rand):
    return mvt + random.randint(-rand,rand)

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

    if paddleTouched(): 
        goingRight=-goingRight
        goingDown=randomizeMovement(goingDown,randomness) #this one) are seemingly the wrong values to change ON PURPOSE
        if xPos>=930:
            xPos=920
        if xPos<=70:
            xPos=80
            
    if xPos>=960:
        scoreL+=1
        xPos=450
        yPos=400
        goingRight=randomizeMovement(0,11)
        goingDown=randomizeMovement(0,11)     
        pause=True
    if xPos<=40:
        xPos=450
        yPos=400
        goingRight=randomizeMovement(0,11)
        goingDown=randomizeMovement(0,11) 
        while not (goingRight<-6 or goingRight>6) and not (goingDown<-4 or goingDown>4):
            goingRight=randomizeMovement(0,11)
            goingDown=randomizeMovement(0,11) 
        scoreR+=1
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
        background.fill(YELLOW.GOLDENROD.full)
        myBallCenterPos = (int(xPos+0.5), int(yPos+0.5)) #normally casting to int goes to next lowest int, adding 0.5 makes behavior like a round
        pygame.draw.circle(background, BLACK.full, myBallCenterPos, 40)
        pygame.draw.rect(background, GREEN.CHARTREUSE.full, paddleLeft)
        pygame.draw.rect(background, GREEN.CHARTREUSE.full, paddleRight)
        goingDown, goingRight = ballCheck(goingDown, goingRight, xPos, yPos)
        xPos, yPos = ballMove(goingDown, goingRight, xPos, yPos)
        
    else: # paused
        
        screen.blit(s, (0,0))    # (0,0) are the top-left coordinates
        screen.blit(pauseText, textpos) # use screen.blit to print to front apparently
    # ALL DA TIME
    
    screen.blit(regularFont.render(str(scoreL), 0, BLUE.ROYALBLUE.full),(50,50))
    screen.blit(regularFont.render(str(scoreR), 0, BLUE.ROYALBLUE.full),(923,50))
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
                paddleY[0]


################################### C H A T ###################################
'''
say your name then a colon, then message

GABRIEL: alex, to use global variables you define them regularly, then to use them 
    in a function, redefine the variable as global inside the function
    
ALEX: ok, i was confused by them so I just did it a different way but thats good to know
ALEX: I don't know if you imported it, but I made a common pygame file thats really useful.
      It initializes everything so you can go straight onto the game loop. It also defines
      a lot of colors as well as a color function so you never really have to define the 
      individual rgb again (you can change a color in side a program btw)
'''
###############################################################################