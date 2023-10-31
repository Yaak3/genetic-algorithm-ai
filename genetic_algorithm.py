import numpy as np

base_distances = np.loadtxt('distances_between_cells.mat')
base_population = np.zeros((20, 20), dtype=int)

def initialize_genetic_algorithm(base_population):
    for row in range(len(base_population)):
        base_population[row] = np.random.choice(np.arange(21), size=len(base_population), replace=False)

initialize_genetic_algorithm(base_population)
