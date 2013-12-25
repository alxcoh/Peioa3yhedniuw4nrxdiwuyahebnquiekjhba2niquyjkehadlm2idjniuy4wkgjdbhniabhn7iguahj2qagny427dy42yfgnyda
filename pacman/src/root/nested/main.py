import pygame
from euclid import Vector2
from math import sin,cos,pi
from random import random

class Thing:
    def __init__(self,pos):
        self.pos = pos
        things.append(self)
    def update(self): pass
    def draw(self,img): pass
    def collide(self,who): pass

class DynamicThing(Thing):
    def __init__(self,pos):
        Thing.__init__(self,pos)
        self.vel = Vector2(0,0)
        self.lastPos = pos
        self.col = (255,255,0)
        self.r = 12
        dynamic_things.append(self)
    def update(self):
        self.lastPos = self.pos
        self.pos = self.pos + self.vel
    def draw(self,img):
        pygame.draw.circle(img, (0,0,0), [int(n) for n in self.pos], self.r, self.r)
        pygame.draw.circle(img, self.col, [int(n) for n in self.pos], self.r-2, self.r-2)
    def collide(self,obj):
        Thing.collide(self,obj)
        if isinstance(obj,Wall): 
            self.pos = self.lastPos

class Wall(Thing):
    def draw(self,img):
        x,y = self.pos.x, self.pos.y
        pygame.draw.rect(img, (90,90,200), (x-16,y-16,32,32), 0)

class Pacman(DynamicThing):
    def __init__(self):
        DynamicThing.__init__(self,Vector2(32*9+16,32*12+16))
        self.col = (255,255,0)
    def update(self):
        DynamicThing.update(self)
        if (keyPressed[pygame.K_LEFT]): self.vel.x = -2
        if (keyPressed[pygame.K_RIGHT]): self.vel.x = 2
        if (keyPressed[pygame.K_DOWN]): self.vel.y = 2
        if (keyPressed[pygame.K_UP]): self.vel.y = -2
        if (self.vel.x==-2 and not keyPressed[pygame.K_LEFT]): self.vel.x = 0
        if (self.vel.x==2 and not keyPressed[pygame.K_RIGHT]): self.vel.x = 0
        if (self.vel.y==2 and not keyPressed[pygame.K_DOWN]): self.vel.y = 0
        if (self.vel.y==-2 and not keyPressed[pygame.K_UP]): self.vel.y = 0
    def collide(self,obj):
        DynamicThing.collide(self,obj)
        if isinstance(obj,Ghost):
            self.pos = Vector2(32*9+16,32*12+16)

class Ghost(DynamicThing):
    def __init__(self):
        DynamicThing.__init__(self,Vector2(32*9+16,32*10+16))
        self.col = (int(random()*255),int(random()*255),int(random()*255))
        self.vel = Vector2(0,-2)
    def update(self):
        DynamicThing.update(self)
        if random()<0.01:
            self.vel = [Vector2(2,0),Vector2(-2,0),Vector2(0,2),Vector2(0,-2)][int(random()*4)]
    def collide(self,obj):
        DynamicThing.collide(self,obj)
        if isinstance(obj,Wall):
            self.vel = [Vector2(2,0),Vector2(-2,0),Vector2(0,2),Vector2(0,-2)][int(random()*4)]

def thingAtPos(pos):
    tile_pos = Vector2(int(pos.x/32),int(pos.y/32))
    return map[tile_pos.y][tile_pos.x]

# initializate stuff
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode([32*19,32*22])
points_in_unit_circle_border = [Vector2(cos(float(a)/8*2*pi),sin(float(a)/8*2*pi)) for a in xrange(8)]
things = []
dynamic_things = []
exit = False

map =  [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
        [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,0,1],
        [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
        [1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,1],
        [1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1],
        [1,1,1,1,0,1,0,1,1,0,1,1,0,1,0,1,1,1,1],
        [1,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,0,1],
        [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1],
        [1,1,1,1,0,1,0,0,0,0,0,0,0,1,0,1,1,1,1],
        [1,1,1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,1],
        [1,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,1],
        [1,0,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,0,1],
        [1,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,1],
        [1,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,1],
        [1,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1],
        [1,0,1,1,1,1,1,1,0,1,0,1,1,1,1,1,0,0,1],
        [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
        [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]


#create pacman, walls, ghosts
pacman = Pacman()
for y in xrange(len(map)):
    for x in xrange(len(map[y])):
        if (map[y][x]==1):
            map[y][x] = Wall(Vector2(x*32+16,y*32+16))
for i in xrange(4):
    Ghost()

while exit==False:
    clock.tick(45)

    screen.fill([255,255,255])
    keyPressed = pygame.key.get_pressed()

    # events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit = True

    # more ghosts
    if random()<0.001: Ghost()

    # updates e draws
    for thing in things:
        thing.update()
        thing.draw(screen)

    # collisions
    for A in dynamic_things:
        #dynamic vs dynamic
        for B in dynamic_things:
            if A!=B and abs(A.pos-B.pos)<(A.r+B.r):
                A.collide(B)
                B.collide(A)
        #dynamic vs walls
        for circle_point in points_in_unit_circle_border:
            thing_in_a_border = thingAtPos(A.pos+circle_point*12)
            if isinstance(thing_in_a_border,Wall):
                A.collide(thing_in_a_border)

    pygame.display.flip()

pygame.quit ()
