import random

# Objective function
def f(x):
    return x * x


def pso():

    # Parameters
    n = 10
    iterations = 20

    w = 0.5
    c1 = 1.5
    c2 = 1.5

    # Initialize particles
    x = []
    v = []

    for i in range(n):
        x.append(random.uniform(-10, 10))
        v.append(random.uniform(-1, 1))

    # Personal best
    pbest = x.copy()

    # Global best
    gbest = min(pbest, key=f)

    # PSO process
    for t in range(iterations):

        for i in range(n):

            r1 = random.random()
            r2 = random.random()

            # Update velocity
            v[i] = (w * v[i]
                    + c1 * r1 * (pbest[i] - x[i])
                    + c2 * r2 * (gbest - x[i]))

            # Update position
            x[i] = x[i] + v[i]

            # Boundary checking
            if x[i] < -10:
                x[i] = -10

            if x[i] > 10:
                x[i] = 10

            # Update personal best
            if f(x[i]) < f(pbest[i]):
                pbest[i] = x[i]

        # Update global best
        current_best = min(pbest, key=f)

        if f(current_best) < f(gbest):
            gbest = current_best

    # Final output
    print("Optimal Solution = {:.10f}".format(gbest))
    print("Objective Function Value = {:.10f}".format(f(gbest)))


pso()
