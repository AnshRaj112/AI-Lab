"""
Write a program to check the initial state and good state of a magic square, with 1 tile missing in both, compute the number of misplaced tiles and give which numbers have been misplaced, user input the initial state and good state.
"""

# Get matrix size from user
n = int(input("Enter the size of the magic square (n x n): "))

# Take input from the user as an n x n matrix
print(f"\nEnter the initial state of the {n}x{n} magic square ({n} rows, enter 'X' or '-' for missing tile):")
initial_matrix = []
for i in range(n):
    while True:
        row = input(f"Row {i+1}: ").split()
        if len(row) == n:
            initial_matrix.append(row)
            break
        else:
            print(f"Please enter exactly {n} elements per row. You entered {len(row)}.")

print(f"\nEnter the good state of the {n}x{n} magic square ({n} rows, enter 'X' or '-' for missing tile):")
good_matrix = []
for i in range(n):
    while True:
        row = input(f"Row {i+1}: ").split()
        if len(row) == n:
            good_matrix.append(row)
            break
        else:
            print(f"Please enter exactly {n} elements per row. You entered {len(row)}.")

# Convert matrix to flat list of integers (replace 'X' or '-' with 0 for missing tile)
initial_state = []
for row in initial_matrix:
    for cell in row:
        if cell.upper() in ['X', '-', '']:
            initial_state.append(-1)
        else:
            initial_state.append(int(cell))

good_state = []
for row in good_matrix:
    for cell in row:
        if cell.upper() in ['X', '-', '']:
            good_state.append(-1)
        else:
            good_state.append(int(cell))

# Compute the number of misplaced tiles and identify which ones
total_tiles = n * n
misplaced_tiles = 0
misplaced_numbers = []

for i in range(total_tiles):
    if initial_state[i] != good_state[i]:
        misplaced_tiles += 1
        misplaced_numbers.append(initial_state[i])

# Print the results
print(f"\nThe number of misplaced tiles is {misplaced_tiles}")

if misplaced_tiles > 0:
    print("The misplaced tiles are:", misplaced_numbers)
    for i in range(total_tiles):
        if initial_state[i] != good_state[i]:
            row = i // n
            col = i % n
            print(f"  Position ({row+1}, {col+1}) [index {i}]: {initial_state[i]} should be {good_state[i]}")
else:
    print("All tiles are in the correct position!")