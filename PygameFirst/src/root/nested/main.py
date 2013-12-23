'''
Created on Dec 22, 2013

@author: alxcoh
'''

import pygame, sys
#from pygame import *
from pygame.locals import *

def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((900, 800))
    pygame.display.set_caption('sqiggity sqag')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
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
    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Invisible Penis Unicorn HA I AM SO SMART", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    while 1: # Event loop
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