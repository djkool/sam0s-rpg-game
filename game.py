import pygame
from pygame.locals import *

pygame.init()

screen=pygame.display.set_mode((660,450))

tiles = pygame.sprite.Group()

world=pygame.image.load('world/r00.png')

clock=pygame.time.Clock()

def getarea(posx,posy):
    x=posx*60
    y=posy*30

    sprite = world.subsurface(pygame.Rect(x, y, 60, 30)) #grabs the sprite at this location

    return sprite

class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
class Controller(object):
    def __init__(self):
        self.area=[0,0]
    def update(self,playerobj):
        if playerobj.x>650:
            self.area[0]+=1
            print "lel"
        tiles.update()
class Player(object):
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def update(self):
        pygame.draw.circle(screen, (0,235,50), (self.x,self.y), 16, 0)
        k=pygame.key.get_pressed()
        if k[K_w]:
            self.y-=5
        if k[K_a]:
            self.x-=5
        if k[K_s]:
            self.y+=5
        if k[K_d]:
            self.x+=5
            
class Tile (Entity): 
    def __init__ (self,x,y,color):
        Entity.__init__(self)
        self.color=color
        self.x=x
        self.y=y
    def update(self):
        pygame.draw.rect(screen, (self.color), (self.x,self.y,16,16), 0)
        
levelsurf=pygame.Surface((660,450))

def CreateLevel(LEVELX,LEVELY):
    levelsurf.fill((0,0,255))
    limage=getarea(LEVELX,LEVELY)
    for j in range(30):
        for i in range(60):
            #print str(i)+","+str(j)
            px = limage.get_at((i,j))
            if px[0]==185:
                #t = Tile(i*16,j*16,(185,122,87))
                pygame.draw.rect(levelsurf, (128,122,87), (i*11,j*15,11,15), 0)
                #tiles.add(t)
            if px[0]==32:
                pygame.draw.rect(levelsurf, (255,255,87), (i*11,j*15,11,15), 0)
                #t = Tile(i*16,j*16,(255,255,0))
                #tiles.add(t)
            if px[2]==176:
                pygame.draw.rect(levelsurf, (239,228,176), (i*11,j*15,11,15), 0)
                #t = Tile(i*16,j*16,(239,228,176))
                #tiles.add(t)
        

go=True
WORLDX=0
WORLDY=0
CreateLevel(0,0)
p=Player(64,64)
c=Controller()


while go:
    pygame.display.set_caption(str(clock.get_fps()))
    screen.fill((0,0,0))
    #c.update(p)
    #screen.blit(limages,(0,0))
    screen.blit(levelsurf,(0,0))
    p.update()
   
    for e in pygame.event.get():
        if e.type == QUIT:
            go = False
    clock.tick(90)
    pygame.display.flip()
    if p.x>640:
        p.x=1
        WORLDX+=1
        CreateLevel(WORLDX,WORLDY)
    if p.x<0:
        p.x=639
        WORLDX-=1
        CreateLevel(WORLDX,WORLDY)
    if p.y<0:
        p.y=479
        WORLDY-=1
        CreateLevel(WORLDX,WORLDY)
    if p.y>480:
        p.y=1
        WORLDY+=1
        CreateLevel(WORLDX,WORLDY)
#print tiles.sprites()

pygame.display.quit()
quit()
    
