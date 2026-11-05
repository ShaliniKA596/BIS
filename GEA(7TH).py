
import random

# 1. Define objective function
def objective(x, y):
    return x**2 + y**2


# 2. Initialize parameters
POP_SIZE = 20
NUM_GENES = 2
MUTATION_RATE = 0.1
CROSSOVER_RATE = 0.8
GENERATIONS = 100

LOWER = -10
UPPER = 10


# 3. Initialize population
def initialize_population():
    population = []

    for i in range(POP_SIZE):
        chromosome = [
            random.uniform(LOWER, UPPER)
            for j in range(NUM_GENES)
        ]
        population.append(chromosome)

    return population


# 4. Gene expression
def gene_expression(chromosome):
    x = chromosome[0]
    y = chromosome[1]

    return x, y


# 5. Fitness evaluation
def fitness(chromosome):
    x, y = gene_expression(chromosome)

    value = objective(x, y)

    return 1 / (1 + value)


# 6. Selection using tournament selection
def selection(population):
    selected = random.sample(population, 3)

    best = max(selected, key=fitness)

    return best[:]


# 7. Crossover
def crossover(parent1, parent2):

    child1 = parent1[:]
    child2 = parent2[:]

    if random.random() < CROSSOVER_RATE:

        point = random.randint(1, NUM_GENES - 1)

        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]

    return child1, child2


# 8. Mutation
def mutation(chromosome):

    for i in range(NUM_GENES):

        if random.random() < MUTATION_RATE:

            chromosome[i] = random.uniform(
                LOWER, UPPER
            )

    return chromosome


# 9. Main Gene Expression Algorithm
def gene_expression_algorithm():

    population = initialize_population()

    best_solution = None
    best_fitness = -1

    for generation in range(GENERATIONS):

        new_population = []

        # Find best chromosome
        current_best = max(population, key=fitness)

        if fitness(current_best) > best_fitness:

            best_fitness = fitness(current_best)
            best_solution = current_best[:]

        # Elitism: preserve best chromosome
        new_population.append(current_best[:])

        # Selection, crossover and mutation
        while len(new_population) < POP_SIZE:

            parent1 = selection(population)
            parent2 = selection(population)

            child1, child2 = crossover(
                parent1, parent2
            )

            child1 = mutation(child1)
            child2 = mutation(child2)

            # Gene expression
            gene_expression(child1)
            gene_expression(child2)

            new_population.append(child1)

            if len(new_population) < POP_SIZE:
                new_population.append(child2)

        population = new_population

        print(
            "Generation:", generation + 1,
            "Best Fitness:", round(best_fitness, 6)
        )

    # Final best solution
    x, y = gene_expression(best_solution)

    print("\n----- FINAL RESULTS -----")
    print("Best Solution:")
    print("X =", round(x, 6))
    print("Y =", round(y, 6))

    print("Minimum Function Value =",
          round(objective(x, y), 6))

    print("Best Fitness =",
          round(best_fitness, 6))


# 10. Execute algorithm
gene_expression_algorithm()
