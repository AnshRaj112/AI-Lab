import random
import math

MUTATION_RATE = 0.15
MIN_GENERATIONS = 3
MAX_GENERATIONS = 50


# -------- USER FUNCTION --------
def user_function(x):
    return eval(FUNCTION)


# -------- Decode Binary --------
def decode(chromosome):
    return int("".join(map(str, chromosome)), 2)


# -------- Encode Decimal --------
def encode(x, bits):
    return list(format(x, f'0{bits}b'))


# -------- Initialize Population --------
def initialize_population(pop_size, bits, lower, upper):
    population = []
    while len(population) < pop_size:
        x = random.randint(lower, upper)
        if user_function(x) != 1:   # avoid optimal initially
            population.append([int(b) for b in format(x, f'0{bits}b')])
    return population


# -------- Print Matrix --------
def print_matrix(population, title):
    print(f"\n{title} (Matrix Form)")
    print("-" * 50)
    for i, chrom in enumerate(population):
        print(f"S{i+1} -> {chrom}")
    print("-" * 50)


# -------- Print Table --------
def print_table(population, title):
    print(f"\n{title}")
    print("-" * 75)
    print(f"{'String':<8}{'Binary':<15}{'Decimal(x)':<15}{'f(x)':<10}")
    print("-" * 75)

    for i, chrom in enumerate(population):
        x = decode(chrom)
        print(f"S{i+1:<7}{''.join(map(str, chrom)):<15}{x:<15}{user_function(x):<10}")
    print("-" * 75)


# -------- Tournament Selection --------
def tournament_selection(population, pop_size):
    print("\nTournament Selection:")
    new_population = []

    for i in range(pop_size):
        a, b = random.sample(range(pop_size), 2)

        x1, x2 = decode(population[a]), decode(population[b])
        f1, f2 = user_function(x1), user_function(x2)

        print(f"Match {i+1}: S{a+1} (f={f1}) vs S{b+1} (f={f2})")

        if f1 < f2:
            new_population.append(population[a].copy())
        else:
            new_population.append(population[b].copy())

    return new_population


# -------- Crossover --------
def crossover(population, pop_size, bits):
    print("\nCrossover:")
    new_population = []

    for i in range(0, pop_size, 2):
        if i+1 < pop_size:
            parent1 = population[i]
            parent2 = population[i+1]

            point = random.randint(1, bits - 1)
            print(f"Crossover S{i+1} & S{i+2} at point {point}")

            child1 = parent1[:point] + parent2[point:]
            child2 = parent2[:point] + parent1[point:]

            new_population.extend([child1, child2])
        else:
            new_population.append(population[i])

    return new_population


# -------- Mutation --------
def mutation(population, bits):
    print("\nMutation:")
    for i in range(len(population)):
        for j in range(bits):
            if random.random() < MUTATION_RATE:
                population[i][j] ^= 1
                print(f"Bit flipped in S{i+1} at position {j}")
    return population


# -------- Main Genetic Algorithm --------
def genetic_algorithm():

    lower = int(input("Enter starting value: "))
    upper = int(input("Enter ending value: "))
    pop_size = int(input("Enter population size: "))

    # Calculate number of bits dynamically
    range_size = upper - lower + 1
    bits = math.ceil(math.log2(range_size))

    print(f"\nNumber of bits required: {bits}")
    print(f"Matrix size: {pop_size} x {bits}")

    population = initialize_population(pop_size, bits, lower, upper)

    generation = 1

    # Store initial best
    initial_best_index = min(
        range(pop_size),
        key=lambda i: user_function(decode(population[i]))
    )

    while generation <= MAX_GENERATIONS:

        print(f"\n\n================ GENERATION {generation} ================")

        print_matrix(population, "Initial Population")
        print_table(population, "Initial Population Details")

        population = tournament_selection(population, pop_size)
        print_table(population, "After Selection")

        population = crossover(population, pop_size, bits)
        print_table(population, "After Crossover")

        population = mutation(population, bits)
        print_table(population, "After Mutation")

        best_index = min(
            range(pop_size),
            key=lambda i: user_function(decode(population[i]))
        )

        best_fx = user_function(decode(population[best_index]))

        if generation >= MIN_GENERATIONS and best_fx == 1:
            print("\nOptimal solution found!")
            break

        generation += 1

    # Final Best
    final_best_index = min(
        range(pop_size),
        key=lambda i: user_function(decode(population[i]))
    )

    final_best = population[final_best_index]
    final_best_x = decode(final_best)
    final_best_fx = user_function(final_best_x)

    print("\n\n================ CONCLUSION ================")
    print(f"Initial Best -> S{initial_best_index+1}, "
          f"x = {decode(population[initial_best_index])}, "
          f"f(x) = {user_function(decode(population[initial_best_index]))}")

    print(f"Final Best   -> S{final_best_index+1}, "
          f"Binary = {''.join(map(str, final_best))}, "
          f"x = {final_best_x}, "
          f"f(x) = {final_best_fx}")

    print(f"Total Generations: {generation}")
    print("Genetic Algorithm successfully minimized the function.")


# -------- User Function Input --------
FUNCTION = input("Enter function in terms of x (example: x**2): ")

genetic_algorithm()