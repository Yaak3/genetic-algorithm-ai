import numpy as np
import random
import math

distances_matrix = np.loadtxt('distances_between_cells.mat')
chromosomes_matrix = np.zeros((20, 20), dtype=int)
number_of_repetitions = 1
count = 0

def initialize_genetic_algorithm(chromosomes_matrix, distances_matrix) -> None:
    initialize_chromosomes(chromosomes_matrix)
    calculate_fitness(chromosomes_matrix, distances_matrix)
    ordering_by_fitness_desc(chromosomes_matrix)

def initialize_chromosomes(chromosomes_matrix) -> None:
    for row in range(len(chromosomes_matrix)):
        chromosomes_matrix[row] = np.random.choice(np.arange(20), size=len(chromosomes_matrix), replace=False)

    return chromosomes_matrix

def calculate_fitness(chromosomes_matrix, distances_matrix) -> None:
    distances  = []
    total_distance = 0

    for chromosome in chromosomes_matrix:
        
        for index in range(len(chromosome)):
            if(index == len(chromosome) - 1):
                total_distance += execute_fitness_calculation(distances_matrix[0][chromosome[-1]], 
                                                              distances_matrix[0][chromosome[-1]],
                                                              distances_matrix[1][chromosome[0]],
                                                              distances_matrix[1][chromosome[0]])
            else:
                total_distance += execute_fitness_calculation(distances_matrix[0][chromosome[index]], 
                                                              distances_matrix[0][chromosome[index]],
                                                              distances_matrix[1][chromosome[index + 1]],
                                                              distances_matrix[1][chromosome[index + 1]])
                
        
        distances.append(total_distance)
        total_distance = 0
    
    return [np.transpose(distances)]
    '''
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
    '''

def randomize_distances(distances_matrix):
    for distance in distances_matrix:
        distance[0] = random.uniform(0, 1)
        distance[1] = random.uniform(0, 1)

def execute_fitness_calculation(origin_chromosome_x, origin_chromosome_y, destiny_chromosome_x, destiny_chromosome_y) -> float:
    return math.sqrt(math.pow(origin_chromosome_x - destiny_chromosome_x, 2) + math.pow(origin_chromosome_y - destiny_chromosome_y, 2))

def ordering_by_fitness_desc(chromosomes_matrix) -> None:
    ordering_indexes = np.argsort(chromosomes_matrix[:, -1])[::-1]
    chromosomes_matrix = chromosomes_matrix[ordering_indexes]


while count < number_of_repetitions:
    chromosomes_matrix = initialize_chromosomes(chromosomes_matrix)
    distances = calculate_fitness(chromosomes_matrix, distances_matrix)
    print(distances)
    chromosomes_matrix = np.hstack((chromosomes_matrix, distances))

    print(chromosomes_matrix)
    count += 1