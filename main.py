import numpy as np
from helper import *

ITERATION_RANGE = 1
distances_matrix = np.loadtxt('distances_between_cells.mat')
chromosomes_matrix = np.zeros((20, 20), dtype=int)

def execute_genetic_algorithm(chromosomes_matrix):
    for _ in range(ITERATION_RANGE):
        chromosomes_matrix = get_best_chromosomes_from_matrix(
            get_chromosomes_ordered_by_fitness(get_chromosomes_merged_with_fitness(chromosomes_matrix, 
                get_calculated_fitness(initialize_chromosomes(chromosomes_matrix), distances_matrix))))
        
        roulette_array = generate_roulette(chromosomes_matrix)
        parrents_array = choose_parents(roulette_array)
        create_children(parrents_array)


execute_genetic_algorithm(chromosomes_matrix)
