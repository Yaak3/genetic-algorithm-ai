import numpy as np
from helper import *

ITERATION_RANGE = 5
distances_matrix = np.loadtxt('distances_between_cells.mat')
chromosomes_matrix = np.zeros((20, 20), dtype=int)
fitness_results = []

def execute_genetic_algorithm(chromosomes_matrix):
    chromosomes_matrix = initialize_chromosomes(chromosomes_matrix)

    for _ in range(ITERATION_RANGE):
        chromosomes_matrix = get_best_chromosomes_from_matrix(
            get_chromosomes_ordered_by_fitness(get_chromosomes_merged_with_fitness(chromosomes_matrix.astype(int), 
                get_calculated_fitness(chromosomes_matrix.astype(int), distances_matrix))))
        childrens_chromosomes = generate_childrens_chromosomes(generate_roulette(chromosomes_matrix))
        fitness_results.append(chromosomes_matrix[0][20])
        chromosomes_matrix = get_new_formed_chromosomes(chromosomes_matrix, childrens_chromosomes)
        print(chromosomes_matrix, '\n\n')

    print(fitness_results)

execute_genetic_algorithm(chromosomes_matrix)
display_fitness_results(fitness_results)
