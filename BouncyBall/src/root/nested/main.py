'''
Created on Dec 23, 2013

@author: alxcoh
'''
import pygame, sys
from pygame.locals import *
#Colors
BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
yPos=450
xPos=400
goingDown=1
goingRight=1
def ballMove():
    if goingDown==1:
        yPos+=8
    if goingDown==0:
        yPos-=8
    if goingRight==1:
        xPos+=8
    if goingRight==0:
        xPos-=8
def ballCheck():
    if yPos>=760:
        goingDown=0
    elif yPos<=40:
        goingDown=1
    if xPos>=860:
        goingRight=0
    elif xPos<=40:
        goingRight=1
def main():
    #Initialization
    pygame.init()
    screen = pygame.display.set_mode((900, 800))
    pygame.display.set_caption('Bouncing Ball')
        
    #Background setup
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(WHITE)
    

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        screen.blit(background, (0, 0))
        background.fill(WHITE)
        myBallCenterPos = (xPos, yPos)
        pygame.draw.circle(background, BLACK, myBallCenterPos, 40)
        ballCheck()
        ballMove()
        pygame.display.flip()
        pygame.display.update()
main()