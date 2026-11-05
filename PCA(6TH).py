
import numpy as np
import matplotlib.pyplot as plt

# 1. Define objective function
def objective(x):
    return np.sum(x ** 2)

# 2. Initialize parameters
ROWS = 5
COLS = 5
DIM = 2
MAX_ITER = 100

LOWER = -10
UPPER = 10

# 3. Initialize population randomly
population = np.random.uniform(
    LOWER, UPPER, (ROWS, COLS, DIM)
)

# Evaluate initial fitness
fitness = np.zeros((ROWS, COLS))

for i in range(ROWS):
    for j in range(COLS):
        fitness[i, j] = objective(population[i, j])

# Store global best solution
best_index = np.unravel_index(
    np.argmin(fitness), fitness.shape
)

global_best = population[best_index].copy()
best_fitness = fitness[best_index]

convergence = []

# 4. Define Von Neumann neighborhood
def get_neighbors(i, j):
    neighbors = []

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for di, dj in directions:
        ni = (i + di) % ROWS
        nj = (j + dj) % COLS
        neighbors.append((ni, nj))

    return neighbors

# 5. Main optimization loop
for iteration in range(MAX_ITER):

    new_population = population.copy()
    new_fitness = fitness.copy()

    # Update all cells using previous iteration states
    for i in range(ROWS):
        for j in range(COLS):

            # Identify neighboring cells
            neighbors = get_neighbors(i, j)

            # Select best neighbor
            best_neighbor = min(
                neighbors,
                key=lambda p: fitness[p]
            )

            neighbor_position = population[best_neighbor]

            # Generate new solution
            r = np.random.rand(DIM)

            new_position = (
                population[i, j]
                + r * (neighbor_position - population[i, j])
                + np.random.normal(0, 0.1, DIM)
            )

            # Apply boundary constraints
            new_position = np.clip(
                new_position, LOWER, UPPER
            )

            # Evaluate new solution
            new_value = objective(new_position)

            # Accept better solution
            if new_value < fitness[i, j]:
                new_population[i, j] = new_position
                new_fitness[i, j] = new_value

    # Update population simultaneously
    population = new_population
    fitness = new_fitness

    # Update global best
    current_best = np.unravel_index(
        np.argmin(fitness), fitness.shape
    )

    if fitness[current_best] < best_fitness:
        best_fitness = fitness[current_best]
        global_best = population[current_best].copy()

    convergence.append(best_fitness)

# 6. Display results
print("Parallel Cellular Optimization Results")
print("--------------------------------------")
print("Best Solution:", global_best)
print("Best Fitness:", best_fitness)
print("Total Iterations:", MAX_ITER)

# 7. Plot convergence graph
plt.plot(convergence, color='blue')
plt.xlabel("Iterations")
plt.ylabel("Best Fitness")
plt.title("PCA Convergence Graph")
plt.grid(True)
plt.show()
