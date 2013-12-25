'''
Created on Dec 23, 2013

@author: alxcoh and 71619997a
'''
from commonFunctions import *
import pygame, sys
from pygame.locals import *
#Colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

crazyball=False #  :D
loopnum=1
yPos=400.0
xPos=450.0
maxDown=16.0
maxRight=16.0
goingDown=8.0
goingRight=8.0
randomness=4 #if you actually want to play crazyball, set this at 4-6 for regular, 6-10 is madness, 10-20 for insanity
crazyDelay=10 #how often velocity changes in crazyball


def randomizeMovement(mvt, rand):
    return mvt + random.randint(-rand,rand)

def ballCheck(a, b, c, d):
    global goingDown
    global goingRight
    global xPos
    global yPos
    global randomness
    goingDown=a
    goingRight=b
    xPos=c
    yPos=d
    if yPos>=660 or yPos<=40:
        goingDown=-goingDown
        goingRight=randomizeMovement(goingRight,randomness) #these two (this and
        if yPos>=660:
            yPos=650
        else:
            yPos=50

    if xPos>=960 or xPos<=40:
        goingRight=-goingRight
        goingDown=randomizeMovement(goingDown,randomness) #this one) are seemingly the wrong values to change ON PURPOSE
        if xPos>=960:
            xPos=950
        else:
            xPos=50
        
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



#Initialization
pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('Bouncing Ball')
    
#Background setup
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)

while True:
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
    background.fill(WHITE)
    myBallCenterPos = (int(xPos+0.5), int(yPos+0.5)) #normally casting to int goes to next lowest int, adding 0.5 makes behavior like a round
    pygame.draw.circle(background, BLACK, myBallCenterPos, 40)
    
    goingDown, goingRight = ballCheck(goingDown, goingRight, xPos, yPos)
    xPos, yPos = ballMove(goingDown, goingRight, xPos, yPos)
    
    pygame.display.flip()
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            break
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                break
        

################################### C H A T ###################################
'''
say your name then a colon, then message

GABRIEL: alex, to use global variables you define them regularly, then to use them 
    in a function, redefine the variable as global inside the function
'''
###############################################################################