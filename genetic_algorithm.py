import numpy as np
import math

ITERATION_RANGE = 1
distances_matrix = np.loadtxt('distances_between_cells.mat')
chromosomes_matrix = np.zeros((20, 20), dtype=int)

def initialize_chromosomes(chromosomes_matrix) -> []:
    for row in range(len(chromosomes_matrix)):
        chromosomes_matrix[row] = np.random.choice(np.arange(20), size=len(chromosomes_matrix), replace=False)
    return chromosomes_matrix

def get_calculated_fitness(chromosomes_matrix, distances_matrix) -> []:
    fitness_utility  = []
    total_distance = 0

    for chromosome in chromosomes_matrix:
        for index in range(len(chromosome)):
            if (index == len(chromosome) - 1):
                total_distance += execute_fitness_calculation(distances_matrix[0][chromosome[-1]], 
                                                              distances_matrix[0][chromosome[-1]],
                                                              distances_matrix[1][chromosome[0]],
                                                              distances_matrix[1][chromosome[0]])
            else:
                total_distance += execute_fitness_calculation(distances_matrix[0][chromosome[index]], 
                                                              distances_matrix[0][chromosome[index]],
                                                              distances_matrix[1][chromosome[index + 1]],
                                                              distances_matrix[1][chromosome[index + 1]])
        fitness_utility.append(total_distance)
        total_distance = 0

    return np.reshape(fitness_utility, (20, 1))

def execute_fitness_calculation(origin_chromosome_x, origin_chromosome_y, destiny_chromosome_x, destiny_chromosome_y) -> float:
    return math.sqrt(math.pow(origin_chromosome_x - destiny_chromosome_x, 2) + math.pow(origin_chromosome_y - destiny_chromosome_y, 2))

def get_chromosomes_merged_with_fitness(chromosomes_matrix, fitness_distances_matrix) -> []:
    return np.hstack((chromosomes_matrix, fitness_distances_matrix))

def get_chromosomes_ordered_by_fitness(chromosomes_matrix) -> []:
    ordering_indexes = np.argsort(chromosomes_matrix[:, -1])[::-1]
    return chromosomes_matrix[ordering_indexes]

def get_best_chromosomes_from_matrix(chromosomes_matrix) -> []:
    return chromosomes_matrix[:10, :]

def generate_roulette(chromosomes_matrix) -> []:
    roulette_array = []
    chromosomes_matrix_len = len(chromosomes_matrix)

    for row in range(chromosomes_matrix_len):
        roulette_array = roulette_array + [chromosomes_matrix[row]] * (chromosomes_matrix_len - row)
    return roulette_array

def execute_genetic_algorithm(chromosomes_matrix):
    for _ in range(ITERATION_RANGE):
        chromosomes_matrix = get_best_chromosomes_from_matrix(
            get_chromosomes_ordered_by_fitness(get_chromosomes_merged_with_fitness(chromosomes_matrix, 
                get_calculated_fitness(initialize_chromosomes(chromosomes_matrix), distances_matrix))))
        roulette_array = generate_roulette(chromosomes_matrix)
        print(roulette_array)

execute_genetic_algorithm(chromosomes_matrix)
