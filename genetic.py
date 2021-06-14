from generartree import drawTree

SILHOUETTE = 0
X1 = 400
Y1 = 550
ANGLE = -90 

class Individual:
    def __init__(self, fitness, depth, init_line_len, decrease_prop, ram_number, ram_angle):
        self.fitness = fitness
        self.depth = depth
        self.init_line_len = init_line_len
        self.decrease_prop = decrease_prop #pendiente de agregar a drawTree
        self.ram_number = ram_number #pendiente de agregar a drawTree
        self.ram_angle = ram_angle
    
    def printTree(self):
        drawTree(X1, Y1, ANGLE, depth, ram_angle, init_line_len)

    def get_percentage_in(self, SILHOUETTE):
        #buenas aqui encuentra porcentaje de pixeles del arb_ind que coinciden con silueta
        value = 0
        return value

    def get_percentage_out(self, SILHOUETTE):
        #buenas aqui encuentra porcentaje de pixeles del arb_ind que no coinciden con silueta
        value = 0
        return value

    def calc_fitness(self, SILHOUETTE): #fitness function
        #! PENDIENTE, PENALIZAR EL TAMAÑO SI ES DEMASIADO PEQUEÑO, qué tan largo es el alcance? 
        # EXTREMOS, probar con eso para ver que tanto esta distribuido
        percentage_in= get_percentage_in(self, SILHOUETTE)
        percentage_out= get_percentage_out(self, SILHOUETTE)

        fitness_value = ( percentage_in - percentage_out ) / 100
        return fitness_value

    def selection(self): #Individual generation[]
        best_fit = 0
        return best_fit 

    def mutate(self):
        mutation = True

    def crossover(self):
        newInd = 0
        return newInd

    #def do_generation():
    #def print_individual():








