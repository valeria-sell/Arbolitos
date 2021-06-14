from genetic import simulation

import pygame, math, random
from pygame.locals import *

simulation() 

def input(event):
    if event.type == pygame.QUIT:
        exit(0)

while True:
    input(pygame.event.wait())

