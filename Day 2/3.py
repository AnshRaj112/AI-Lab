"""
Write a program to calculate the degree of each vertex in an undirected graph.(input-adjacency matrix, output degree of each vertex, user fed matrix)
"""

from graph_utils import get_adjacency_matrix_input, display_adjacency_matrix, calculate_degrees_from_matrix


def main():
    """Main function to calculate the degree of each vertex."""
    # Take input from the user
    adjacency_matrix = get_adjacency_matrix_input()
    
    # Print the adjacency matrix
    display_adjacency_matrix(adjacency_matrix)
    
    # Print the degree of each vertex
    print(f"Degrees: {calculate_degrees_from_matrix(adjacency_matrix)}")


if __name__ == "__main__":
    main()