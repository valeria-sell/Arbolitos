from genetic import simulation

import pygame, math, random
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()

simulation(window, screen) 

def input(event):
    if event.type == pygame.QUIT:
        exit(0)

while True:
    input(pygame.event.wait())

