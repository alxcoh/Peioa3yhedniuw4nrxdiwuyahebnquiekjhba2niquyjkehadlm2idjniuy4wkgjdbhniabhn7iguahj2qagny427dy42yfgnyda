'''
Created on Dec 23, 2013

@author: alxcoh
'''
import pygame, sys
from pygame.locals import *
from commonFunctions import *
class color():
    def __init__(self, r, g, b):
        self.r=r
        self.g=g
        self.b=b 
        self.full=pygame.Color(r, g, b)

class BLUE(color):
    def __init__(self):
        color(0,0,255)
    NAVYBLUE = color(0, 0, 128)
    ROYALBLUE = color(8, 76, 158)
    MEDIUMBLUE = color(0, 0, 205)
    AZURE = color(0, 127, 255)
    CYAN = color(0, 255, 255)
    SKYBLUE = color(0,180,255)
    AQUAMARINE = color(127, 255, 212)
    TEAL = color(0, 128, 128)

class GREEN(color):
    def __init__(self):
        color(0, 255, 0)
    FORESTGREEN = color(34, 139, 34)
    OLIVE = color(128, 128, 0)
    CHARTREUSE = color(127, 255, 0)
    LIME = color(191, 255, 0)
    AQUAMARINE = color(127, 255, 212)
    TEAL = color(0, 128, 128)
    CYAN = color(0, 255, 255)
    
class RED(color):
    def __init__(self):
        color(255, 0, 0)
    SALMON = color(250, 128, 114)
    HOTPINK = color(252, 15, 192)
    FUCHSIA = color(255, 119, 255)
    PUCE = color(204, 136, 153)
    MAUVE = color(224, 176, 255)
    LAVENDER = color(181, 126, 220)
    PLUM = color(132, 49, 121)
    MAROON = color(128, 0, 0)
    CRIMSON = color(220, 20, 60)
    VIOLET = color(143, 0, 255)
    CORAL = color(255, 127, 80)
    
    
class GRAY(color):
    def __init__(self):
        color(128, 128, 128)    
    IVORY = color(255, 255, 240)
    BEIGE = color(245, 245, 220)
    WHEAT = color(245, 222, 179)
    TAN = color(210, 180, 140)
    KHAKI = color(195, 176, 145)
    SILVER = color(192, 192, 192)
    CHARCOAL = color(70, 70, 70)
    
    
class YELLOW(color):
    def __init__(self):
        color(255, 255, 0)
    GOLD = color(255, 215, 0)
    GOLDENROD = color(218, 165, 32)
    KHAKI = color(195, 176, 145)
    
#color definitions

BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)
'''IVORY = color(255, 255, 240)
BEIGE = color(245, 245, 220)
WHEAT = color(245, 222, 179)
TAN = color(210, 180, 140)
KHAKI = color(195, 176, 145)
SILVER = color(192, 192, 192)
GRAY = color(128, 128, 128)
CHARCOAL = color(70, 70, 70)
'''

GOLD = color(255, 215, 0)
GOLDENROD = color(218, 165, 32)


#Initialization
pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('Bouncing Ball')
        
#Background setup
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(WHITE.full)

'''
REMEMBER TO PUT THIS EVERYWHERE
for event in pygame.event.get():
            if event.type == QUIT:
                return
'''