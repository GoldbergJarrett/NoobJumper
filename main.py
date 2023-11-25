import pygame, sys
from pygame.locals import *

pygame.init()
vec = pygame.math.Vector2

WINDOW_HEIGHT = 450
WINDOW_WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60
 
FramePerSec = pygame.time.Clock()
 
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Noob Jumper")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
   
        self.pos = vec((10, 385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def move(self):
        self.acc = vec(0,0)
    
        pressed_keys = pygame.key.get_pressed()
                
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WINDOW_WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WINDOW_WIDTH
            
        self.rect.midbottom = self.pos
        
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WINDOW_WIDTH, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT - 10))
 
PT1 = platform()
P1 = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
     
    window.fill((0,0,0))
 
    P1.move()

    for entity in all_sprites:
        window.blit(entity.surf, entity.rect)
 
    pygame.display.update()
    FramePerSec.tick(FPS)