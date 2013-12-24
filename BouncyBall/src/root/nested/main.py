'''
Created on Dec 23, 2013

@author: alxcoh
'''
import pygame, sys
from pygame.locals import *
#Colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)

global yPos
global xPos
global goingDown
global goingRight
yPos=400
xPos=450
goingDown=1
goingRight=1

def ballCheck(a, b, c, d):
    goingDown=a
    goingRight=b
    xPos=c
    yPos=d
    if yPos>=760:
        goingDown=0
    elif yPos<=40:
        goingDown=1
    if xPos>=860:
        goingRight=0
    elif xPos<=40:
        goingRight=1
    return goingDown, goingRight

def ballMove(a, b, c, d):
    goingDown=a
    goingRight=b
    xPos=c
    yPos=d
    if goingRight==1:
        xPos+=8
    if goingRight==0:
        xPos-=8
    if goingDown==1:
        yPos+=8
    if goingDown==0:
        yPos-=8
    return xPos, yPos
#Initialization
pygame.init()
screen = pygame.display.set_mode((900, 800))
pygame.display.set_caption('Bouncing Ball')
        
#Background setup
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)

def main():
    #Variables
    xPos=450
    yPos=400
    goingDown=1
    goingRight=1

    
    
    

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        screen.blit(background, (0, 0))
        background.fill(WHITE)
        myBallCenterPos = (xPos, yPos)
        pygame.draw.circle(background, BLACK, myBallCenterPos, 40)
        
        goingDown, goingRight = ballCheck(goingDown, goingRight, xPos, yPos)
        xPos, yPos = ballMove(goingDown, goingRight, xPos, yPos)
        
        pygame.display.flip()
        pygame.display.update()
main()