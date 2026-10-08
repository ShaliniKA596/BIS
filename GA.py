import random

# Objective function
# Maximize f(x) = x^2
def fitness(x):
    return x * x


# Genetic Algorithm
def genetic_algorithm():

    # Parameters
    population_size = 10
    generations = 20
    mutation_rate = 0.1

    # Generate initial population
    population = []

    for i in range(population_size):
        population.append(random.randint(0, 31))

    print("Initial Population:", population)

    # Genetic Algorithm
    for generation in range(generations):

        # Evaluate fitness
        population.sort(key=fitness, reverse=True)

        # Selection
        parents = population[:5]

        # Create new population
        new_population = []

        # Keep best solution
        new_population.append(parents[0])

        while len(new_population) < population_size:

            # Select parents
            p1 = random.choice(parents)
            p2 = random.choice(parents)

            # Crossover
            child = (p1 + p2) // 2

            # Mutation
            if random.random() < mutation_rate:
                child = random.randint(0, 31)

            new_population.append(child)

        population = new_population

    # Find best solution
    best = max(population, key=fitness)

    # Display result
    print("\nOptimal Solution =", best)
    print("Optimal Fitness  =", fitness(best))


# Execute
genetic_algorithm()
