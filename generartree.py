##Fuente: https://rosettacode.org/wiki/Fractal_tree#Python
import pygame, math
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()

def drawTree(x1, y1, angle, depth, ram_angle, init_line_len): #Falta incluir ram_number
    #angle is upright (-90)
    #ram_angle es el angulo de las ramificaciones
    if depth > 0:
        #?Encontrar donde se define la proporcion de decremento de line en cada nivel
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * init_line_len)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * init_line_len)
        pygame.draw.line(screen, (255,255,255), (x1, y1), (x2, y2),2)
        drawTree(x2, y2, angle - ram_angle, depth - 1, ram_angle, init_line_len)
        drawTree(x2, y2, angle + ram_angle, depth - 1, ram_angle, init_line_len)
def input(event):
    if event.type == pygame.QUIT:
        exit(0)

#drawtree recibe x, y, angulo de posicion y profundidad de ramas
#!auxilio diferencia entre numero de ramificaciones y los niveles? 
#!porque el numero de ramif puede ser random?
nombre = "11"
drawTree(100, 195, -90, 14, 7, 2.0)
pygame.image.save(window, "palitos/"+nombre+".jpg")
pygame.display.flip()
while True:
    input(pygame.event.wait())