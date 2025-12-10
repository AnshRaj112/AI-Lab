"""
Write a program to check whether two vertices are directly connected or not.
(input-adjacency matrix, user fed matrix)
"""

from graph_utils import get_adjacency_matrix_input, display_adjacency_matrix, are_vertices_connected_matrix


def main():
    """Main function to check if two vertices are directly connected."""
    # Take input from the user
    adjacency_matrix = get_adjacency_matrix_input()
    
    # Print the adjacency matrix
    display_adjacency_matrix(adjacency_matrix)
    
    # Get the two vertices to check
    vertex1 = int(input("Enter the first vertex: "))
    vertex2 = int(input("Enter the second vertex: "))
    
    # Check if they are directly connected
    is_connected = are_vertices_connected_matrix(adjacency_matrix, vertex1, vertex2)
    
    # Print the result
    if is_connected:
        print(f"Vertices {vertex1} and {vertex2} are directly connected.")
    else:
        print(f"Vertices {vertex1} and {vertex2} are NOT directly connected.")


if __name__ == "__main__":
    main()
