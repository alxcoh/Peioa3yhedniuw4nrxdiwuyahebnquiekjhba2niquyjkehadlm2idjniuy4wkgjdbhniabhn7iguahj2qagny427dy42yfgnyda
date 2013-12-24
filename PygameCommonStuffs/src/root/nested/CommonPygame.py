'''
Created on Dec 23, 2013

@author: alxcoh
'''
import pygame, sys
from pygame.local import *

BLACK = pygame.Color(0, 0, 0)
WHITE = pygame.Color(255, 255, 255)
IVORY = pygame.Color(255, 255, 240)
BEIGE = pygame.Color(245, 245, 220)
WHEAT = pygame.Color(245, 222, 179)
TAN = pygame.Color(210, 180, 140)


#Initialization
pygame.init()
screen = pygame.display.set_mode((900, 800))
pygame.display.set_caption('Bouncing Ball')
        
#Background setup
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE)


'''
REMEMBER TO PUT THIS EVERYWHERE
for event in pygame.event.get():
            if event.type == QUIT:
                return
'''