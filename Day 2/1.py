"""
write a function oriented program to calculate the number of edges in an undirected graph.(input-adjacency matrix, output number of edges, user fed matrix)
"""

def count_edges(adjacency_matrix):
    num_edges = 0
    for i in range(len(adjacency_matrix)):
        for j in range(i+1, len(adjacency_matrix)):
            if adjacency_matrix[i][j] == 1:
                num_edges += 1
    return num_edges

# Take input from the user
num_vertices = int(input("Enter the number of vertices: "))
adjacency_matrix = []
for i in range(num_vertices):
    row = list(map(int, input(f"Enter the row {i+1}: ").split()))
    adjacency_matrix.append(row)

# Print the adjacency matrix
print("Adjacency Matrix:")
for row in adjacency_matrix:
    print(row)

# Print the number of edges
print(f"Number of edges: {count_edges(adjacency_matrix)}")