import numpy as np
from random import randint
import matplotlib.pyplot as plt
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
    ordering_indexes = np.argsort(chromosomes_matrix[:, -1])
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

def choose_parents_chromosomes(roulette_array) -> []:
    parents_chromosomes = []
    roulette_array_len = len(roulette_array)

    while (len(parents_chromosomes) < 2):
        parents_chromosomes.clear()
        parents_chromosomes.append(roulette_array[randint(0, roulette_array_len - 1)])
        second_parent_index = randint(0, roulette_array_len - 1)

        if (not np.array_equal(parents_chromosomes[0], roulette_array[second_parent_index])):  
            parents_chromosomes.append(roulette_array[second_parent_index])      
        continue
    return parents_chromosomes

def generate_childrens_chromosomes(roulette_array) -> []:
    childrens_chromosomes = []
    chromosome_merge_complete = None
    parent_a_value = 0
    parent_b_value = 0
    gene_index = 0

    for _ in range(5):
        chromosome_merge_complete = False
        parents_chromosomes = choose_parents_chromosomes(roulette_array)
        gene_index = randint(0, 19)

        while(~chromosome_merge_complete):
            parent_a_value = parents_chromosomes[0][gene_index]
            parent_b_value = parents_chromosomes[1][gene_index]

            parents_chromosomes[0][gene_index] = parent_b_value
            parents_chromosomes[1][gene_index] = parent_a_value

            repeat_indices = np.where(parents_chromosomes[0] == parent_b_value)[0]

            if(len(repeat_indices) > 1):
                gene_index = repeat_indices[np.where(repeat_indices != gene_index)[0][0]]
            else:
                chromosome_merge_complete = True
                childrens_chromosomes.extend([parents_chromosomes[0], parents_chromosomes[1]])

    return childrens_chromosomes

def get_new_formed_chromosomes(chromosomes_matrix, childrens_chromosomes) -> []:
    return np.concatenate((chromosomes_matrix[:, :-1], childrens_chromosomes))

def display_fitness_results(fitness_results) -> None:
    plt.pie(fitness_results, autopct='%1.1f%%', startangle=90)
    plt.title('Fitness Results')
    plt.show()
