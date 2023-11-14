import numpy as np
from random import randint
import math

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
    chromosomes_matrix_without_fitness = chromosomes_matrix[:, :-1]
    chromosomes_matrix_len = len(chromosomes_matrix)

    for row in range(chromosomes_matrix_len):
        roulette_array = roulette_array + [chromosomes_matrix_without_fitness[row]] * (chromosomes_matrix_len - row)
    return roulette_array

def choose_parents(roulette_array) -> []:
    parents = []
    first_parent = None
    second_parent = None
    rand = 0

    for _ in range(5):
        rand = randint(0, len(roulette_array) - 1)

        first_parent = roulette_array[rand]
        parents.append(first_parent)

        rand = randint(0, len(roulette_array) - 1)
        second_parent = roulette_array[rand]

        while(np.array_equal(first_parent, second_parent)):        
            rand = randint(0, len(roulette_array) - 1)
            second_parent = roulette_array[rand]

        parents.append(second_parent)
    
    return parents

def create_children(parrents):
    childrens = []
    rand = 0
    parent_a = None
    parent_b = None
    value_parent_a = 0
    value_parent_b = 0

    for index in range(0,9,2):
        parent_a = parrents[index]
        parent_b = parrents[index + 1]
        rand = randint(0,19)

        value_parent_a = parent_a[rand]
        value_parent_b = parent_b[rand]

        parent_a[rand] = value_parent_b
        parent_b[rand] = value_parent_a

        unique, count = np.unique(parent_a, return_counts=True)
        #Falta verificar onde está o valor repetido e trocar ele depois
        while(np.any(count > 1)):
            pass


        break

        
