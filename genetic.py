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
        self.decrease_prop = decrease_prop
        self.ram_number = ram_number #pendiente de agregar a drawTree
        self.ram_angle = ram_angle
        self.printTree()
    
    def printTree(self):
        d_depth = random.randint(self.depth[0], self.depth[1])
        d_ram_angle = random.randint(self.ram_angle[0] , self.ram_angle[1])
        d_line_len = random.randint(self.line_len[0] , self.line_len[1])
        d_decrease_prop = random.randint(self.decrease_prop[0] , self.decrease_prop[1])
        drawTree(d_depth, d_ram_angle, d_line_len, d_decrease_prop)
        #save_and_show()

    def get_percentage_in(self):
        #buenas aqui encuentra porcentaje de pixeles del arb_ind que coinciden con silueta
        global SILHOUETTE
        value = 1
        return value

    def get_percentage_out(self):
        #buenas aqui encuentra porcentaje de pixeles del arb_ind que no coinciden con silueta
        global SILHOUETTE
        value = 1
        return value

    def calc_fitness(self): #fitness function
        #! PENDIENTE, PENALIZAR EL TAMAÑO SI ES DEMASIADO PEQUEÑO, qué tan largo es el alcance? 
        # EXTREMOS, probar con eso para ver que tanto esta distribuido
        percentage_in = self.get_percentage_in()
        percentage_out = self.get_percentage_out()

        fitness_value = ( percentage_in - percentage_out ) / 100
        self.fitness = fitness_value

    #Individual generation[]
    def selection(self, generation): 
        ranking = []
        for i in generation:
            ranking.append(i)
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


def simulation():
    #Prueba de arbolito ------------------------------------------------------------------------
    nombre = "11"

    depth = [5 , 14]
    ram_angle = [4 , 30]
    line_len = [1.0 , 2.0]
    decrease_prop = [1, 9]

    d_depth = random.randint(depth[0], depth[1])
    d_ram_angle = random.randint(ram_angle[0] , ram_angle[1])
    d_line_len = random.randint(line_len[0] , line_len[1])
    d_decrease_prop = random.randint(decrease_prop[0] , decrease_prop[1])

    drawTree(d_depth, d_ram_angle, d_line_len, d_decrease_prop)
    save_and_show(nombre)
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
        indiv.calc_fitness()
    



    






