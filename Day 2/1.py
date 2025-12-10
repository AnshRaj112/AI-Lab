"""
write a function oriented program to calculate the number of edges in an undirected graph.(input-adjacency matrix, output number of edges, user fed matrix)
"""

from graph_utils import get_adjacency_matrix_input, display_adjacency_matrix, count_edges_from_matrix


def main():
    """Main function to calculate the number of edges."""
    # Take input from the user
    adjacency_matrix = get_adjacency_matrix_input()
    
    # Print the adjacency matrix
    display_adjacency_matrix(adjacency_matrix)
    
    # Print the number of edges
    print(f"Number of edges: {count_edges_from_matrix(adjacency_matrix)}")


if __name__ == "__main__":
    main()