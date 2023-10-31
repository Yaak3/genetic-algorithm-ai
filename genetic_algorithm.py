import numpy as np
from random import randint

distancias = np.loadtxt('distancias.mat')

initial_pop = []

for initital_pop in range(19):
    individual = []
    while(len(individual) != 19):
        random_city = randint(0,20)

        if(random_city not in individual):
            individual.append(random_city)

    initial_pop.append(individual)

print(len(initial_pop))