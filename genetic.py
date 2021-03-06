import random, cv2, os
import numpy as np
from generartree import drawTree, save_and_show
from operator import attrgetter

SILHOUETTE = 0
GEN_SIZE = 12
TOURNAMENT_SIZE = 2 #SELECTION METHOD
GEN_HISTORY = []
GEN_VERSION = 1
GEN_LIMIT = 10
GENERATION = []
MUTATION_PROB = 2 #% OUT OF GEN SIZE

X1 = 100
Y1 = 195
ANGLE = -90 

class Individual:
    def __init__(self, identification, checked_status, fitness, depth, line_len, decrease_prop_diam, ram_number, ram_angle):
        self.id = identification
        self.checked_status = checked_status
        self.fitness = fitness
        self.depth = depth
        self.line_len = line_len
        self.decrease_prop_diam = decrease_prop_diam
        self.ram_number = ram_number 
        self.ram_angle = ram_angle
        self.printTree()
    
    def printTree(self):
        d_ram_number = self.ram_number
        d_depth = int(random.uniform(self.depth[0], self.depth[1]))
        d_ram_angle = int(random.uniform(self.ram_angle[0] , self.ram_angle[1]))
        d_line_len = int(random.uniform(self.line_len[0] , self.line_len[1]))
        d_decrease_prop_diam = int(random.uniform(self.decrease_prop_diam[0] , self.decrease_prop_diam[1]))
        drawTree(d_ram_number, d_depth, d_ram_angle, d_line_len, d_decrease_prop_diam)
        #save_and_show() estamos pendientes de la creacion del atributo nombre

    def set_id(self, name):
        self.id = name

    def get_id(self):
        return str(self.id)

    def get_status(self):
        return self.checked_status

    def change_status(self):
        change = self.checked_status
        self.checked_status = not change

    def get_percentage_in(self):
        #buenas aqui encuentra porcentaje de pixeles del arb_ind que coinciden con silueta
        global SILHOUETTE
        value = 0
        value = count_pixels(self.comparation()[1])
        value = ((value)*100)/200*200
        return value

    def get_percentage_out(self):
        #buenas aqui encuentra porcentaje de pixeles del arb_ind que no coinciden con silueta
        global SILHOUETTE
        value = 0
        value = count_pixels(self.comparation()[1])
        value = ((value)*100)/200*200
        return value

    def calc_fitness(self): #fitness function
        #! PENDIENTE, PENALIZAR EL TAMA??O SI ES DEMASIADO PEQUE??O, qu?? tan largo es el alcance? 
        # EXTREMOS, probar con eso para ver que tanto esta distribuido
        percentage_in = self.get_percentage_in()
        percentage_out = self.get_percentage_out()

        fitness_value = ( percentage_in - percentage_out ) / 100
        self.fitness = fitness_value

    #This method mutates the individual itself, generating new values of decrease prop, ram_number, ram_angle, depth
    def mutate(self): 
        mutation_value = random.random()
        if (mutation_value > 0.0):
            start = random.randint(0 , 9)
            end = random.randint(start , 10)
            self.decrease_prop_diam = [start , end]
        if (mutation_value > 0.2):
            start = random.randint(0 , 4)
            end = random.randint(start , 5)
            self.init_line_len = [start , end]
        if (mutation_value > 0.6):
            start = random.randint(0 , 30)
            end = random.randint(start , 31)
            self.ram_angle = [start , end]
        if (mutation_value > 0.8):
            start = random.randint(0 , 9)
            end = random.randint(start , 10)
            self.depth = [start , end]

    def comparation(self):
        arbolito = cv2.imread("palitos/tree0.jpg", 1)
        fractal = cv2.imread("palitos/"+self.id+".jpg", 1)
        resultIn = cv2.subtract(arbolito, fractal)
        resultOut = cv2.subtract(arbolito, resultIn)
        return [resultIn, resultOut]

def count_pixels(matrix):
    matrix_in = matrix[0]
    matrix_in[-1] = 69
    matrix_out = matrix[1]
    matrix_out[-1] = 69
    num_pixels_in = 0
    num_pixels_out = 0
    count = 0
    for i in range(len(matrix_in)-1): #i es una natriz
        for j in(matrix_in[i]):
            count = count + j
        if (count == 765):
            num_pixels_in += 1 
    count = 0
    for i in range(len(matrix_out)-1): #i es una natriz
        for j in(matrix_out[i]):
            count = count + j
        if (count == 765):
            num_pixels_out += 1 

def may_mutate(n):
    #Prob of mutation is MUTATION_PROB
    #Population/ total is GEN_SIZE
    #Chances are 
    chances = ((10-MUTATION_PROB)/100)*GEN_SIZE
    if ((n/10) >= chances):
        GENERATION[n].mutate
        print ("Alguien mut??")

def survivor_episode(children):
    GENERATION.sort(key=attrgetter('fitness'))
    children = children + (len(GENERATION) - 1) -1
    GENERATION[:children]

    #only 1 new child per GENERATION
def crossover(mother, father):
    depth = []
    for i in range(0 , 2):
        depth.insert(i, ((mother.depth[i] + father.depth[i]) / 2))
    line_len = []
    for i in range(0 , 2):
        line_len.insert(i, ((mother.line_len[i] + father.line_len[i]) / 2))
    decrease_prop_diam = []
    for i in range(0 , 2):
        decrease_prop_diam.insert(i, ((mother.decrease_prop_diam[i] + father.decrease_prop_diam[i]) / 2))
    ram_number = [0,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3]
    ram_angle = []
    for i in range(0 , 2):
        ram_angle.insert(i, ((mother.ram_angle[i] + father.ram_angle[i]) / 2))

    newInd = Individual(0, False, 0, depth, line_len, decrease_prop_diam, ram_number, ram_angle)
    return newInd

def selection(): 
    #Sort individuals randomly in 2 groups 
    groupA = []
    groupB = []
    finalists = []
    best_parents = []

    for i in GENERATION:
        rand_value = random.randint(0,1)
        if (rand_value == 1):
            if (len(groupA) < (len(GENERATION)/TOURNAMENT_SIZE)):
                groupA.append(i)
            else:
                groupB.append(i)
        else:
            if (len(groupB) < (len(GENERATION)/TOURNAMENT_SIZE)):
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

def treeTest():
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

    #drawTree(d_ram_number, d_depth, d_ram_angle, d_line_len, d_decrease_prop_diam)
    #save_and_show(nombre)
    #fin de prueba-----------------------------------------------------------------------------

def simulation():
    global GEN_VERSION
    treeTest()
    # generate First Class
    
    for i in range(GEN_SIZE):
        start = random.randint(0 , 9)
        end = random.randint(start , 10)
        decrease_prop_diam = [start , end]

        start = random.randint(0 , 9)
        end = random.randint(start , 10)
        line_len = [start , end]

        start = random.randint(0 , 3)
        end = random.randint(start , 4)
        ram_number = [0,1,1,2,2,2,2,2,2,2,2,2,3,3,3,3,3,3,3,3]

        start = random.randint(0 , 30)
        end = random.randint(start , 31)
        ram_angle = [start , end]

        start = random.randint(0 , 9)
        end = random.randint(start , 10)
        depth = [start , end]

        tree = Individual(0, False, 0, depth, line_len, decrease_prop_diam, ram_number, ram_angle)
        GENERATION.append(tree)
        #drawTree(d_ram_number, d_depth, d_ram_angle, d_line_len, d_decrease_prop_diam)
        tree.set_id("1" + str(i))
        save_and_show("1",str(i))
    #print (GENERATION[0])

    # Asign proper fitness value
    for indiv in GENERATION:
        indiv.calc_fitness()
    
    print(GENERATION[0].comparation(0))
    
    #Save copy of gen in history for later
    GEN_HISTORY.append(GENERATION)
    GEN_VERSION += 1

    #Begin Selection Process, if more than one child is desired then loop next two lines
    parents = selection()
    newInd = crossover(parents[0], parents[1])
    newInd.set_id(str(GEN_VERSION) + "1")
    save_and_show(str(GEN_VERSION), "1")
    newInd.calc_fitness()
    GENERATION.append(newInd)
    survivor_episode(1)

    while (GEN_VERSION < GEN_LIMIT):
        GEN_HISTORY.append(GENERATION)
        GEN_VERSION += 1

        #mutation step
        n = random.randint(0,13)
        may_mutate(n)

        #Begin Selection Process, if more than one child is desired then loop next two lines
        parents = selection()
        newInd = crossover(parents[0], parents[1])
        newInd.set_id(str(GEN_VERSION) + "1")
        save_and_show(str(GEN_VERSION), "1")
        newInd.calc_fitness()
        GENERATION.append(newInd)
        survivor_episode(1)

        print(newInd.id)
        
    GENERATION.sort(key=attrgetter('fitness'))
    print("Mejor Figura", GENERATION[0].id)

    #and repeat
    
    



    






