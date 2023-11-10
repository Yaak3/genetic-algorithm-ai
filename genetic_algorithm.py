import numpy as np
import math

ITERATION_RANGE = 1
distances_matrix = np.loadtxt('distances_between_cells.mat')
chromosomes_matrix = np.zeros((20, 20), dtype=int)

def initialize_chromosomes(chromosomes_matrix) -> []:
    for row in range(len(chromosomes_matrix)):
        chromosomes_matrix[row] = np.random.choice(np.arange(20), size=len(chromosomes_matrix), replace=False)

    return chromosomes_matrix

def calculate_fitness(chromosomes_matrix, distances_matrix) -> []:
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

def get_chromosomes_ordered_by_fitness(chromosomes_matrix) -> []:
    ordering_indexes = np.argsort(chromosomes_matrix[:, -1])[::-1]
    return chromosomes_matrix[ordering_indexes]

def get_best_chromosomes_from_matrix(chromosomes_matrix) -> []:
    return chromosomes_matrix[:10, :]

for _ in range(ITERATION_RANGE):
    # arrumar essa parada de ficar retornando umonte de vezes
    # faltaria a roleta pra criar os filhos, e depois a mutacao?
    chromosomes_matrix = initialize_chromosomes(chromosomes_matrix)
    fitness_distances_matrix = calculate_fitness(chromosomes_matrix, distances_matrix)
    chromosomes_matrix = np.hstack((chromosomes_matrix, fitness_distances_matrix))
    chromosomes_matrix = get_chromosomes_ordered_by_fitness(chromosomes_matrix)
    chromosomes_matrix = get_best_chromosomes_from_matrix(chromosomes_matrix)

'''
    def initialize_genetic_algorithm(chromosomes_matrix, distances_matrix) -> None:
        initialize_chromosomes(chromosomes_matrix)
        calculate_fitness(chromosomes_matrix, distances_matrix)
        ordering_by_fitness_desc(chromosomes_matrix)

    fitness_utility_matrix = np.zeros((20, 1), dtype=float)
    fitness_unitary_results = []

    for row in range(len(chromosomes_matrix)):
        randomize_distances(distances_matrix)

        for column in range(len(chromosomes_matrix) - 1):
            fitness_unitary_results.append(execute_fitness_calculation(
                distances_matrix[column][0], distances_matrix[column][1],
                distances_matrix[column + 1][0], distances_matrix[column + 1][1]))

        fitness_utility_matrix[row] = sum(fitness_unitary_results)
        fitness_unitary_results.clear()

    chromosomes_matrix = np.hstack((chromosomes_matrix, fitness_utility_matrix))


def randomize_distances(distances_matrix) -> None:
    for distance in distances_matrix:
        distance[0] = random.uniform(0, 1)
        distance[1] = random.uniform(0, 1)
'''
