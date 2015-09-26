import pygame
from pygame.locals import *

from level import *

class Controller(object):
    def __init__(self):
        self.area=[0,0]
    def update(self,playerobj):
        if playerobj.x>650:
            self.area[0]+=1
            print "lel"
        tiles.update()


class Player(Entity):
    def __init__(self,x,y):
        Entity.__init__(self, x, y)
    def update(self):
        k=pygame.key.get_pressed()
        if k[K_w]:
            self.y-=5
        if k[K_a]:
            self.x-=5
        if k[K_s]:
            self.y+=5
        if k[K_d]:
            self.x+=5

    def render(self, surf):
        screen_pos = (self.x % SCREEN_SIZE[0], self.y % SCREEN_SIZE[1])
        pygame.draw.circle(surf, (0,235,50), screen_pos, 16, 0)


SCREEN_SIZE = (660,450)
DESIRED_FPS = 90

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)
tiles = pygame.sprite.Group()
world = Level(SCREEN_SIZE, "r00.png")
clock = pygame.time.Clock()

go=True
p=Player(64,64)
c=Controller()


while go:
    pygame.display.set_caption(str(clock.get_fps()))

    # updates
    #c.update(p)
    #screen.blit(limages,(0,0))
    p.update()

    # Keep player from leaving game world
    # This should eventually be moved into Player
    if p.x < 0:
        p.x = 1
    elif p.x >= world.size[0]:
        p.x = world.size[0] - 1
    if p.y < 0:
        p.y = 1
    elif p.y >= world.size[1]:
        p.y = world.size[1] - 1

    world.move((p.x, p.y))
   
    for e in pygame.event.get():
        if e.type == QUIT:
            go = False

    # render
    screen.fill((0,0,0))
    world.render(screen)
    p.render(screen)
    pygame.display.flip()

    clock.tick(DESIRED_FPS)

#print tiles.sprites()

pygame.display.quit()
quit()
    
