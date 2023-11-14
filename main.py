import numpy as np
from helper import *

ITERATION_RANGE = 2
distances_matrix = np.loadtxt('distances_between_cells.mat')
chromosomes_matrix = np.zeros((20, 20), dtype=int)
best_fitnesses = []

def execute_genetic_algorithm(chromosomes_matrix):
    for _ in range(ITERATION_RANGE):
        chromosomes_matrix = get_best_chromosomes_from_matrix(
            get_chromosomes_ordered_by_fitness(get_chromosomes_merged_with_fitness(chromosomes_matrix, 
                get_calculated_fitness(initialize_chromosomes(chromosomes_matrix), distances_matrix))))
        childrens_chromosomes = generate_childrens_chromosomes(generate_roulette(chromosomes_matrix))
        best_fitnesses.append(chromosomes_matrix[0][20])
        chromosomes_matrix = get_new_formed_chromosomes(chromosomes_matrix, childrens_chromosomes)
        print(chromosomes_matrix)

    print(best_fitnesses)

execute_genetic_algorithm(chromosomes_matrix)
