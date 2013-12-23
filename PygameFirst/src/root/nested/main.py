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
    pygame.display.set_caption('Basic Pygame program')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    r=255
    g=0
    b=255
    
    #r-=1
    # Display some text
    font = pygame.font.Font(None, 36)
    text = font.render("Hello There", 1, (10, 10, 10))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    greaterR=0
    greaterG=0
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

        screen.blit(background, (0, 0))
        pygame.display.flip()


main()