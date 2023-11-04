import numpy as np
import math

distances_matrix = np.transpose(np.loadtxt('distances_between_cells.mat'))
chromosomes_matrix = np.zeros((20, 20), dtype=float)

def initialize_genetic_algorithm(chromosomes_matrix, distances_matrix) -> None:
    initialize_chromosomes(chromosomes_matrix)
    calculate_fitness(chromosomes_matrix, distances_matrix)
    ordering_by_fitness_desc(chromosomes_matrix)

def initialize_chromosomes(chromosomes_matrix) -> None:
    for row in range(len(chromosomes_matrix)):
        chromosomes_matrix[row] = np.random.choice(np.arange(21), size=len(chromosomes_matrix), replace=False)

def calculate_fitness(chromosomes_matrix, distances_matrix) -> None:
    # no caso, a gente teria q randomizar os [x,y] das  celulas
    fitness_utility_matrix = np.zeros((20, 1), dtype=float)
    fitness_unitary_results = []

    for row in range(len(chromosomes_matrix)):
        for column in range(len(chromosomes_matrix) - 1):
            fitness_unitary_results.append(execute_fitness_calculation(
                distances_matrix[column][0], distances_matrix[column][1],
                distances_matrix[column + 1][0], distances_matrix[column + 1][1]))

        fitness_utility_matrix[row] = sum(fitness_unitary_results)
        fitness_unitary_results.clear()

    chromosomes_matrix = np.hstack((chromosomes_matrix, fitness_utility_matrix))

def execute_fitness_calculation(origin_chromosome_x, origin_chromosome_y, destiny_chromosome_x, destiny_chromosome_y) -> float:
    return math.sqrt(math.pow(origin_chromosome_x - destiny_chromosome_x, 2) + math.pow(origin_chromosome_y - destiny_chromosome_y, 2))

def ordering_by_fitness_desc(chromosomes_matrix) -> None:
    ordering_indexes = np.argsort(chromosomes_matrix[:, -1])[::-1]
    chromosomes_matrix = chromosomes_matrix[ordering_indexes]

initialize_genetic_algorithm(chromosomes_matrix, distances_matrix)
