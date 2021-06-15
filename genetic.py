import random
import pygame, math
from generartree import drawTree, save_and_show
from operator import attrgetter

SILHOUETTE = 0
GEN_SIZE = 12
TOURNAMENT_SIZE = 2 #SELECTION METHOD

X1 = 100
Y1 = 195
ANGLE = -90 

class Individual:
    def __init__(self, fitness, depth, line_len, decrease_prop_diam, ram_number, ram_angle):
        self.fitness = fitness
        self.depth = depth
        self.line_len = line_len
        self.decrease_prop_diam = decrease_prop_diam
        self.ram_number = ram_number 
        self.ram_angle = ram_angle
        self.printTree()
    
    def printTree(self):
        d_ram_number = self.ram_number
        d_depth = random.randint(self.depth[0], self.depth[1])
        d_ram_angle = random.randint(self.ram_angle[0] , self.ram_angle[1])
        d_line_len = random.randint(self.line_len[0] , self.line_len[1])
        d_decrease_prop_diam = random.randint(self.decrease_prop_diam[0] , self.decrease_prop_diam[1])
        drawTree(d_ram_number, d_depth, d_ram_angle, d_line_len, d_decrease_prop_diam)
        #save_and_show() estamos pendientes de la creacion del atributo nombre

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
            start = random.randint(0 , 3)
            end = random.randint(start , 4)
            self.ram_number = [start , end]
        if (mutation_value > 0.6):
            start = random.randint(0 , 30)
            end = random.randint(start , 31)
            self.ram_angle = [start , end]
        if (mutation_value > 0.8):
            start = random.randint(0 , 10)
            end = random.randint(start , 11)
            self.depth = [start , end]

    #only 1 new child per generation
    def crossover(self, mother, father, generation):
        depth = []
        for i in range(2):
            depth.insert(i, ((mother.depth[i] + father.depth[i]) / 2))
        line_len = []
        for i in range(2):
            line_len.insert(i, ((mother.line_len[i] + father.line_len[i]) / 2))
        decrease_prop = []
        for i in range(2):
            decrease_prop.insert(i, ((mother.decrease_prop[i] + father.decrease_prop[i]) / 2))
        ram_number = [] 
        for i in range(2):
            ram_number.insert(i, ((mother.ram_number[i] + father.ram_number[i]) / 2))
        ram_angle = []
        for i in range(2):
            ram_angle.insert(i, ((mother.ram_angle[i] + father.ram_angle[i]) / 2))

        newInd = Individual(0, depth, line_len, decrease_prop, ram_number, ram_angle)
        generation.append(newInd)
    #def do_generation():

def selection(generation): 
    #Sort individuals randomly in 2 groups 
    groupA = []
    groupB = []
    finalists = []
    best_parents = []

    for i in generation:
        rand_value = random.randint(0,1)
        if (rand_value == 1):
            if (len(groupA) < (len(generation)/TOURNAMENT_SIZE)):
                groupA.append(i)
            else:
                groupB.append(i)
        else:
            if (len(groupB) < (len(generation)/TOURNAMENT_SIZE)):
                groupB.append(i)
            else:
                groupA.append(i)
            
    #Find 2 best in both groups and add to finalists
    groupA.sort(key=attrgetter('fitness'))
    groupB.sort(key=attrgetter('fitness'))
    for i in range(0, TOURNAMENT_SIZE):
        finalists.append(groupA[i])
        finalists.append(groupB[i])

    #Select 2 best from finalists
    finalists.sort(key=attrgetter('fitness'))
    best_parents = finalists[:TOURNAMENT_SIZE]

    #print(best_parents)
    #Return best parents
    return best_parents

def simulation():
    #Prueba de arbolito ------------------------------------------------------------------------
    nombre = "11"

    d_ram_number = [0,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3]
    depth = [5 , 14]
    ram_angle = [4 , 30]
    line_len = [1.0 , 4.0]
    decrease_prop_diam = [1, 9]

    d_depth = random.randint(depth[0], depth[1])
    d_ram_angle = random.randint(ram_angle[0] , ram_angle[1])
    d_line_len = random.randint(line_len[0] , line_len[1])
    d_decrease_prop_diam = random.randint(decrease_prop_diam[0] , decrease_prop_diam[1])

    drawTree(d_ram_number, d_depth, d_ram_angle, d_line_len, d_decrease_prop_diam)
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

        start = random.randint(0 , 3)
        end = random.randint(start , 4)
        ram_number = [0,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3]

        start = random.randint(0 , 30)
        end = random.randint(start , 31)
        ram_angle = [start , end]

        start = random.randint(0 , 10)
        end = random.randint(start , 11)
        depth = [start , end]

        tree = Individual(0, depth, line_len, decrease_prop, ram_number, ram_angle)
        generation.append(tree)

    print (generation)

    # Asign proper fitness value
    for indiv in generation:
        indiv.calc_fitness()
    
    #Begin Selection Process
    selection(generation)
    
    



    






