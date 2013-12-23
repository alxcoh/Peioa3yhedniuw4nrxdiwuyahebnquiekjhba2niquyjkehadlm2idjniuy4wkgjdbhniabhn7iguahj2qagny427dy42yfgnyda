'''
Created on Dec 22, 2013

@author: alxcoh
'''

import pygame, sys
#from pygame import *
from pygame.locals import *

def main():
    # Initialize screen
    pygame.init()
    screen = pygame.display.set_mode((900, 800))
    pygame.display.set_caption('sqiggity sqag')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
<<<<<<< HEAD
    topR=252
    lowR=3
    topB=252
    lowB=3
    topG=252
    lowG=3
    rUp=True
    gUp=False
    bUp=True
    rIter=4
    bIter=2
    gIter=3
    r=89
    g=89
    b=89
    background.fill((r, g, b))
=======
    r=255
    g=0
    b=255
    
    #r-=1
>>>>>>> 2200568b8717175bc26cbdac47249005b4d4a3c9
    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Invisible Penis Unicorn HA I AM SO SMART", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

<<<<<<< HEAD
    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

=======
    greaterR=0
    greaterG=0
>>>>>>> 2200568b8717175bc26cbdac47249005b4d4a3c9
    while 1: # Event loop
        background.fill((r, g, b))
        if r==0:
            greaterR=1
        elif r==255:
            greaterR=0
        if greaterR==0:
            r-=1
        elif greaterR==1:
            r+=1
        if g==0:
            greaterG=1
        elif g==255:
            greaterG=0
        if greaterG==0:
            g-=1
        elif greaterG==1:
            g+=1
        for event in pygame.event.get():
            if event.type == QUIT:
                return
        if r<=lowR or r>=topR:
            rUp=not rUp
        if g<=lowG or g>=topG:
            gUp=not gUp
        if b<=lowB or b>=topB:
            bUp=not bUp
        if rUp:
            r+=rIter
        else:
            r-=rIter
        if gUp:
            g+=gIter
        else:
            g-=gIter
        if bUp:
            b+=bIter
        else:
            b-=bIter
            
            
        background.fill((r, g, b))
        screen.blit(background, (0, 0))
        screen.blit(text, textpos)
        pygame.display.flip()


main()