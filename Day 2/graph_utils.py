"""
Utility functions for graph operations:
- User input for adjacency matrix
- User input for adjacency list
- Conversion functions between adjacency matrix and adjacency list
- Display functions
"""

def get_adjacency_matrix_input():
    """
    Get adjacency matrix input from user.
    Returns: adjacency matrix (list of lists)
    """
    num_vertices = int(input("Enter the number of vertices: "))
    adjacency_matrix = []
    for i in range(num_vertices):
        row = list(map(int, input(f"Enter the row {i+1}: ").split()))
        adjacency_matrix.append(row)
    return adjacency_matrix


def get_adjacency_list_input():
    """
    Get adjacency list input from user.
    Returns: adjacency list (list of lists, where each inner list contains neighbors)
    """
    num_vertices = int(input("Enter the number of vertices: "))
    adjacency_list = []
    for i in range(num_vertices):
        neighbors = list(map(int, input(f"Enter neighbors of vertex {i}: ").split()))
        adjacency_list.append(neighbors)
    return adjacency_list


def display_adjacency_matrix(adjacency_matrix):
    """
    Display the adjacency matrix in a readable format.
    """
    print("Adjacency Matrix:")
    for row in adjacency_matrix:
        print(row)


def display_adjacency_list(adjacency_list):
    """
    Display the adjacency list in a readable format.
    """
    print("Adjacency List:")
    for i, neighbors in enumerate(adjacency_list):
        print(f"Vertex {i}: {neighbors}")


def adjacency_matrix_to_list(adjacency_matrix):
    """
    Convert adjacency matrix to adjacency list.
    Returns: adjacency list
    """
    num_vertices = len(adjacency_matrix)
    adjacency_list = []
    for i in range(num_vertices):
        neighbors = []
        for j in range(num_vertices):
            if adjacency_matrix[i][j] == 1:
                neighbors.append(j)
        adjacency_list.append(neighbors)
    return adjacency_list


def adjacency_list_to_matrix(adjacency_list):
    """
    Convert adjacency list to adjacency matrix.
    Returns: adjacency matrix
    """
    num_vertices = len(adjacency_list)
    adjacency_matrix = [[0] * num_vertices for _ in range(num_vertices)]
    for i, neighbors in enumerate(adjacency_list):
        for neighbor in neighbors:
            adjacency_matrix[i][neighbor] = 1
    return adjacency_matrix


def count_edges_from_matrix(adjacency_matrix):
    """
    Count the number of edges in an undirected graph from adjacency matrix.
    Returns: number of edges
    """
    num_edges = 0
    for i in range(len(adjacency_matrix)):
        for j in range(i+1, len(adjacency_matrix)):
            if adjacency_matrix[i][j] == 1:
                num_edges += 1
    return num_edges


def count_edges_from_list(adjacency_list):
    """
    Count the number of edges in an undirected graph from adjacency list.
    In an undirected graph, each edge is counted twice (once from each endpoint),
    so we sum all the degrees and divide by 2.
    Returns: number of edges
    """
    total_degree = sum(len(neighbors) for neighbors in adjacency_list)
    num_edges = total_degree // 2
    return num_edges

def calculate_degrees_from_matrix(adjacency_matrix):
    """
    Calculate the degree of each vertex in an undirected graph from adjacency matrix.
    Returns: list of degrees
    """
    num_vertices = len(adjacency_matrix)
    degrees = [0] * num_vertices
    for i in range(num_vertices):
        for j in range(num_vertices):
            if adjacency_matrix[i][j] == 1:
                degrees[i] += 1
    return degrees

def calculate_degrees_from_list(adjacency_list):
    """
    Calculate the degree of each vertex in an undirected graph from adjacency list.
    Returns: list of degrees
    """
    num_vertices = len(adjacency_list)
    degrees = [0] * num_vertices
    for i in range(num_vertices):
        degrees[i] = len(adjacency_list[i])
    return degrees


def are_vertices_connected_matrix(adjacency_matrix, vertex1, vertex2):
    """
    Check whether two vertices are directly connected in an undirected graph from adjacency matrix.
    Returns: True if connected, False otherwise
    """
    num_vertices = len(adjacency_matrix)
    if vertex1 < 0 or vertex1 >= num_vertices or vertex2 < 0 or vertex2 >= num_vertices:
        return False
    return adjacency_matrix[vertex1][vertex2] == 1


def are_vertices_connected_list(adjacency_list, vertex1, vertex2):
    """
    Check whether two vertices are directly connected in an undirected graph from adjacency list.
    Returns: True if connected, False otherwise
    """
    num_vertices = len(adjacency_list)
    if vertex1 < 0 or vertex1 >= num_vertices or vertex2 < 0 or vertex2 >= num_vertices:
        return False
    return vertex2 in adjacency_list[vertex1]


def check_path_exists_matrix(adjacency_matrix, path_sequence):
    """
    Check if there exists a path with the given sequence of nodes from adjacency matrix.
    Returns: (True, path_length) if path exists, (False, -1) otherwise
    """
    if len(path_sequence) < 2:
        return (False, -1)
    
    num_vertices = len(adjacency_matrix)
    
    # Check if all vertices in the sequence are valid
    for vertex in path_sequence:
        if vertex < 0 or vertex >= num_vertices:
            return (False, -1)
    
    # Check if consecutive vertices in the sequence are connected
    for i in range(len(path_sequence) - 1):
        vertex1 = path_sequence[i]
        vertex2 = path_sequence[i + 1]
        if adjacency_matrix[vertex1][vertex2] != 1:
            return (False, -1)
    
    # Path length is number of edges, which is number of vertices - 1
    path_length = len(path_sequence) - 1
    return (True, path_length)


def check_path_exists_list(adjacency_list, path_sequence):
    """
    Check if there exists a path with the given sequence of nodes from adjacency list.
    Returns: (True, path_length) if path exists, (False, -1) otherwise
    """
    if len(path_sequence) < 2:
        return (False, -1)
    
    num_vertices = len(adjacency_list)
    
    # Check if all vertices in the sequence are valid
    for vertex in path_sequence:
        if vertex < 0 or vertex >= num_vertices:
            return (False, -1)
    
    # Check if consecutive vertices in the sequence are connected
    for i in range(len(path_sequence) - 1):
        vertex1 = path_sequence[i]
        vertex2 = path_sequence[i + 1]
        if vertex2 not in adjacency_list[vertex1]:
            return (False, -1)
    
    # Path length is number of edges, which is number of vertices - 1
    path_length = len(path_sequence) - 1
    return (True, path_length)