import random
import pygame, math
from generartree import drawTree, save_and_show

SILHOUETTE = 0
GEN_SIZE = 10
TOURNAMENT_SIZE = 3 #SELECTION METHOD

X1 = 100
Y1 = 195
ANGLE = -90 

class Individual:
    def __init__(self, fitness, depth, line_len, decrease_prop, ram_number, ram_angle):
        self.fitness = fitness
        self.depth = depth
        self.line_len = line_len
        self.decrease_prop = decrease_prop #pendiente de agregar a drawTree
        self.ram_number = ram_number #pendiente de agregar a drawTree
        self.ram_angle = ram_angle
    
    def printTree(self):
        d_depth = random.randint(self.depth[0], self.depth[1])
        d_ram_angle = random.randint(self.ram_angle[0] , self.ram_angle[1])
        d_line_len = random.randint(self.line_len[0] , self.line_len[1])
        drawTree(X1, Y1, ANGLE, d_depth, d_ram_angle, d_line_len)

    def get_percentage_in(self, SILHOUETTE):
        #buenas aqui encuentra porcentaje de pixeles del arb_ind que coinciden con silueta
        value = 1
        return value

    def get_percentage_out(self, SILHOUETTE):
        #buenas aqui encuentra porcentaje de pixeles del arb_ind que no coinciden con silueta
        value = 1
        return value

    def calc_fitness(self, SILHOUETTE): #fitness function
        #! PENDIENTE, PENALIZAR EL TAMAÑO SI ES DEMASIADO PEQUEÑO, qué tan largo es el alcance? 
        # EXTREMOS, probar con eso para ver que tanto esta distribuido
        percentage_in = 0 #get_percentage_in(SILHOUETTE)
        percentage_out = 0 #get_percentage_out(SILHOUETTE)

        fitness_value = ( percentage_in - percentage_out ) / 100
        self.fitness = fitness_value

    #Individual generation[]
    def selection(self): 
        best_fit = 0
        return best_fit 

    #This method mutates the individual itself, generating new values of decrease prop, ram_number, ram_angle, depth
    def mutate(self): 
        mutation_value = random.random()
        if (mutation_value > 0.0):
            start = random.randint(0 , 50)
            end = random.randint(start , 51)
            self.decrease_prop = [start , end]
        if (mutation_value > 0.2):
            start = random.randint(0 , 4)
            end = random.randint(start , 5)
            self.init_line_len = [start , end]
        if (mutation_value > 0.4):
            start = random.randint(0 , 10)
            end = random.randint(start , 11)
            self.ram_number = [start , end]
        if (mutation_value > 0.6):
            start = random.randint(0 , 30)
            end = random.randint(start , 31)
            self.ram_angle = [start , end]
        if (mutation_value > 0.8):
            start = random.randint(0 , 10)
            end = random.randint(start , 11)
            self.depth = [start , end]

    def crossover(self):
        newInd = 0
        return newInd

    #def do_generation():


def simulation(window, screen):
    #Prueba de arbolito ------------------------------------------------------------------------
    nombre = "11"

    depth = [5 , 14]
    ram_angle = [4 , 30]
    line_len = [1.0 , 2.0]

    d_depth = random.randint(depth[0], depth[1])
    d_ram_angle = random.randint(ram_angle[0] , ram_angle[1])
    d_line_len = random.randint(line_len[0] , line_len[1])

    drawTree(X1, Y1, ANGLE, d_depth, d_ram_angle, d_line_len)
    save_and_show(window, nombre)
    #fin de prueba-----------------------------------------------------------------------------

    # generate First Class
    generation = []
    for i in range(GEN_SIZE):
        start = random.randint(0 , 50)
        end = random.randint(start , 51)
        decrease_prop = [start , end]

        start = random.randint(0 , 9)
        end = random.randint(start , 10)
        line_len = [start , end]

        start = random.randint(0 , 10)
        end = random.randint(start , 11)
        ram_number = [start , end]

        start = random.randint(0 , 30)
        end = random.randint(start , 31)
        ram_angle = [start , end]

        start = random.randint(0 , 10)
        end = random.randint(start , 11)
        depth = [start , end]
        tree = Individual(0, depth, line_len, decrease_prop, ram_number, ram_angle)
        generation.append(tree)
    print (generation)

    for indiv in generation:
        indiv.calc_fitness(SILHOUETTE)
    



    






