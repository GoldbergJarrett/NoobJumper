import pygame
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