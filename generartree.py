##Fuente: https://rosettacode.org/wiki/Fractal_tree#Python
import pygame, math, random
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((200, 200))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()

def drawTree(ram_number, depth, ram_angle, line_len, prop_decr):
    pygame.Surface.fill(window,(255,255,255))
    x1 = 100
    x2 = 195
    angle = -90
    drawTreeAUX(x1, x2, ram_number, angle, depth, ram_angle, line_len, prop_decr)

def drawTreeAUX(x1, y1, ram_number, angle, depth, ram_angle, line_len, prop_decr):
    #angle is upright (-90)
    #ram_angle es el angulo de las ramificaciones
    if depth > 0:
        d_ram_number = random.randint(0,19)
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * line_len)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * line_len)
        pygame.draw.line(screen, (0,0,0), (x1, y1), (x2, y2), prop_decr)
        if(prop_decr != 1 and line_len > 0.2):
            if(ram_number[d_ram_number] == 1):
                if(random.randint(0,1) == 0):
                    drawTreeAUX(x2, y2, ram_number, angle - ram_angle, depth - 1, ram_angle, line_len, prop_decr-1)
                else:
                    drawTreeAUX(x2, y2, ram_number, angle + ram_angle, depth - 1, ram_angle, line_len, prop_decr-1)
            elif(ram_number[d_ram_number] == 2):
                drawTreeAUX(x2, y2, ram_number, angle - ram_angle, depth - 1, ram_angle, line_len, prop_decr-1)
                drawTreeAUX(x2, y2, ram_number, angle + ram_angle, depth - 1, ram_angle, line_len, prop_decr-1)
            elif(ram_number[d_ram_number] == 3):
                drawTreeAUX(x2, y2, ram_number, angle - ram_angle, depth - 1, ram_angle, line_len, prop_decr-1)
                drawTreeAUX(x2, y2, ram_number, angle, depth - 1, ram_angle, line_len, prop_decr-1)
                drawTreeAUX(x2, y2, ram_number, angle + ram_angle, depth - 1, ram_angle, line_len, prop_decr-1)
        else:
            if(ram_number[d_ram_number] == 1):
                if(random.randint(0,1) == 0):
                    drawTreeAUX(x2, y2, ram_number, angle - ram_angle, depth - 1, ram_angle, line_len, 1)
                else:
                    drawTreeAUX(x2, y2, ram_number, angle + ram_angle, depth - 1, ram_angle, line_len, 1)
            elif(ram_number[d_ram_number] == 2):
                drawTreeAUX(x2, y2, ram_number, angle - ram_angle, depth - 1, ram_angle, line_len, 1)
                drawTreeAUX(x2, y2, ram_number, angle + ram_angle, depth - 1, ram_angle, line_len, 1)
            elif(ram_number[d_ram_number] == 3):
                drawTreeAUX(x2, y2, ram_number, angle - ram_angle, depth - 1, ram_angle, line_len, 1)
                drawTreeAUX(x2, y2, ram_number, angle, depth - 1, ram_angle, line_len, 1)
                drawTreeAUX(x2, y2, ram_number, angle + ram_angle, depth - 1, ram_angle, line_len, 1)

def save_and_show(generacion, numero):
    pygame.image.save(window, "palitos/"+generacion+numero+".jpg")
    pygame.Surface.fill(window,(255,255,255))