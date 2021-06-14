##Fuente: https://rosettacode.org/wiki/Fractal_tree#Python
import pygame, math
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()

def drawTree(depth, ram_angle, line_len, prop_decr):
    x1 = 100
    x2 = 195
    angle = -90
    drawTreeAUX(x1, x2, angle, depth, ram_angle, line_len, prop_decr)

def drawTreeAUX(x1, y1, angle, depth, ram_angle, line_len, prop_decr): #Falta incluir ram_number
    #angle is upright (-90)
    #ram_angle es el angulo de las ramificaciones
    if depth > 0:
        #?Encontrar donde se define la proporcion de decremento de line en cada nivel
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * line_len)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * line_len)
        pygame.draw.line(screen, (255,255,255), (x1, y1), (x2, y2), prop_decr)
        if(prop_decr != 1):
            drawTreeAUX(x2, y2, angle - ram_angle, depth - 1, ram_angle, line_len, prop_decr-1)
            drawTreeAUX(x2, y2, angle + ram_angle, depth - 1, ram_angle, line_len, prop_decr-1)
        else:
            drawTreeAUX(x2, y2, angle - ram_angle, depth - 1, ram_angle, line_len, 1)
            drawTreeAUX(x2, y2, angle + ram_angle, depth - 1, ram_angle, line_len, 1)

def save_and_show(nombre):
    pygame.image.save(window, "palitos/"+nombre+".jpg")
    pygame.display.flip()