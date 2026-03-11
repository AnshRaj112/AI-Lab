import random

N = 5
POP_SIZE = 4
MAX_GENERATIONS = 200

# Generate a chromosome (1-indexed positions)
def generate_chromosome():
    return random.sample(range(1, N + 1), N)

print(generate_chromosome())

# Display chromosome as a 2D board
def display_board(chromosome, prefix=""):
    if prefix:
        print(prefix)
    for row in range(N):
        line = ""
        for col in range(N):
            if chromosome[col] == row + 1:
                line += " Q "
            else:
                line += " . "
        print(line)
    print()

# Helper to get board as array of strings for side-by-side display
def get_board_str(chromosome):
    lines = []
    for row in range(N):
        line = ""
        for col in range(N):
            if chromosome[col] == row + 1:
                line += " Q "
            else:
                line += " . "
        lines.append(line)
    return lines

# Fitness function: number of safe queens (not attacked by any other)
def fitness(chromosome):
    safe_queens = 0
    for i in range(N):
        is_safe = True
        for j in range(N):
            if i != j:
                if chromosome[i] == chromosome[j] or abs(chromosome[i] - chromosome[j]) == abs(i - j):
                    is_safe = False
                    break
        if is_safe:
            safe_queens += 1
    return safe_queens


# Tournament Selection
def tournament_selection(population):
    a = random.choice(population)
    b = random.choice(population)

    # Use fitness values to decide
    if fitness(a) > fitness(b):
        winner = a
    else:
        winner = b

    print(f"Tournament between {a} and {b} Winner: {winner}")
    board_a = get_board_str(a)
    board_b = get_board_str(b)
    board_win = get_board_str(winner)
    
    for i in range(N):
        middle = " and  " if i == N//2 else "      "
        win_mid = " Winner: " if i == N//2 else "         "
        print(f"{board_a[i]}{middle}{board_b[i]}{win_mid}{board_win[i]}")

    return winner


# Ordered Crossover (Permutation Preserving)
def crossover(parent1, parent2):
    size = len(parent1)
    a, b = sorted(random.sample(range(size), 2))
    
    child = [None] * size
    child[a:b] = parent1[a:b]
    
    ptr = b
    for item in parent2:
        if item not in child:
            if ptr >= size:
                ptr = 0
            child[ptr] = item
            ptr += 1
            
    return child


# Swap Mutation (Permutation Preserving)
def mutation(chromosome):
    i, j = random.sample(range(N), 2)
    chromosome[i], chromosome[j] = chromosome[j], chromosome[i]
    return chromosome


# Initial Population
population = [generate_chromosome() for _ in range(POP_SIZE)]

print("Initial Population:")
for i, chrom in enumerate(population):
    display_board(chrom, f"Individual {i+1} (Fitness: {fitness(chrom)}):")

for generation in range(MAX_GENERATIONS):

    print(f"\n--- Generation {generation} ---")

    new_population = []

    # Sort population by fitness to track best
    population.sort(key=fitness, reverse=True)
    best_fitness = fitness(population[0])
    
    print(f"Current Best Fitness: {best_fitness}")
    

    # Elitism: keep the best individual
    new_population.append(population[0])

    while len(new_population) < POP_SIZE:
        parent1 = tournament_selection(population)
        parent2 = tournament_selection(population)

        child = crossover(parent1, parent2)

        if random.random() < 0.2:
            child = mutation(child)

        new_population.append(child)
        print(f"Child: {child} Fitness: {fitness(child)}")
        display_board(child)

    population = new_population

    # Check for solution at the end of the generation
    population.sort(key=fitness, reverse=True)
    if fitness(population[0]) == N:
        print(f"\nSolution Found in Generation {generation}!")
        display_board(population[0])
        break

print("\nFinal Population (Top Performers):")
population.sort(key=fitness, reverse=True)
best_final = fitness(population[0])
for i, chrom in enumerate(population):
    if fitness(chrom) == best_final:
        display_board(chrom, f"Top Individual {i+1} (Fitness {fitness(chrom)}):")