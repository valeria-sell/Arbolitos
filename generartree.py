##Fuente: https://rosettacode.org/wiki/Fractal_tree#Python
import pygame, math
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()

def drawTree(x1, y1, angle, depth):
    #angle is upright (-90)
    #ram_angle es el angulo de las ramificaciones
    ram_angle = 17
    init_line_len = 10.0
    if depth > 0:
        #?Encontrar donde se define la proporcion de decremento de line en cada nivel
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * init_line_len)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * init_line_len)
        pygame.draw.line(screen, (255,255,255), (x1, y1), (x2, y2),2)
        drawTree(x2, y2, angle - ram_angle, depth - 1)
        drawTree(x2, y2, angle + ram_angle, depth - 1)

def input(event):
    if event.type == pygame.QUIT:
        exit(0)

#drawtree recibe x, y, angulo de posicion y profundidad de ramas
#!auxilio diferencia entre numero de ramificaciones y los niveles? 
#!porque el numero de ramif puede ser random?
drawTree(400, 550, -90, 10)
pygame.display.flip()
while True:
    input(pygame.event.wait())