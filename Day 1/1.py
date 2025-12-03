"""
Write a program to print the adjacency matrix and adjacency list of a graph. Where the number of vertices, edges and edge values are given by the user.
"""

# Take input from the user
num_vertices = int(input("Enter the number of vertices: "))
num_edges = int(input("Enter the number of edges: "))

# Get edge values from user
edges = []
print("Enter edge values (format: u v or u,v):")
for i in range(num_edges):
    edge_input = input(f"Edge {i+1}: ").strip()
    # Handle both space-separated and comma-separated input
    if ',' in edge_input:
        u, v = map(int, edge_input.split(','))
    else:
        u, v = map(int, edge_input.split())
    edges.append((u, v))

# Create an adjacency matrix 
adjacency_matrix = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

# Create an adjacency list 
adjacency_list = [[] for _ in range(num_vertices)]

# Populate adjacency matrix and list with edges
for u, v in edges:
    # Add edge to adjacency matrix (undirected graph)
    adjacency_matrix[u][v] = 1
    adjacency_matrix[v][u] = 1
    
    # Add edge to adjacency list
    adjacency_list[u].append(v)
    adjacency_list[v].append(u)

# Print adjacency matrix
print("\nAdjacency Matrix:")
for row in adjacency_matrix:
    print(row)

# Print adjacency list
print("\nAdjacency List:")
for i, neighbors in enumerate(adjacency_list):
    print(f"Vertex {i}: {neighbors}")