##Fuente: https://rosettacode.org/wiki/Fractal_tree#Python
import pygame, math
from pygame.locals import *

def drawTree(x1, y1, angle, depth, ram_angle, init_line_len): #Falta incluir ram_number
    import main
    NSCREEN = main.screen
    #angle is upright (-90)
    #ram_angle es el angulo de las ramificaciones
    if depth > 0:
        #?Encontrar donde se define la proporcion de decremento de line en cada nivel
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * init_line_len)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * init_line_len)
        pygame.draw.line(NSCREEN, (255,255,255), (x1, y1), (x2, y2),2)
        drawTree(x2, y2, angle - ram_angle, depth - 1, ram_angle, init_line_len)
        drawTree(x2, y2, angle + ram_angle, depth - 1, ram_angle, init_line_len)

def save_and_show(window, nombre):
    pygame.image.save(window, "palitos/"+nombre+".jpg")
    pygame.display.flip()


