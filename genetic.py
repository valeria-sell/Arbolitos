#Esqueleto función fitness
def get_percentage_in(tree, silhouette):
    #buenas aqui encuentra porcentaje de pixeles del arb_ind que coinciden con silueta
    value = 0
    return value

def get_percentage_out(tree, silhouette):
    #buenas aqui encuentra porcentaje de pixeles del arb_ind que no coinciden con silueta
    value = 0
    return value

def calc_fitness(tree, silhouette):
    #! PENDIENTE, PENALIZAR EL TAMAÑO SI ES DEMASIADO PEQUEÑO 
    percentage_in= get_percentage_in(tree, silhouette)
    percentage_out= get_percentage_out(tree, silhouette)

    fitness_value = ( percentage_in - percentage_out ) / 100
    return fitness_value
