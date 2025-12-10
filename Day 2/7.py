"""
Write a program to check if there exists a path with the given sequence of nodes.
If yes, find out the length of the path.
(input-adjacency matrix, user fed matrix)
"""

from graph_utils import get_adjacency_matrix_input, display_adjacency_matrix, check_path_exists_matrix


def main():
    """Main function to check if a path exists with given sequence of nodes."""
    # Take input from the user
    adjacency_matrix = get_adjacency_matrix_input()
    
    # Print the adjacency matrix
    display_adjacency_matrix(adjacency_matrix)
    
    # Get the sequence of nodes
    path_sequence = list(map(int, input("Enter the sequence of nodes (space-separated): ").split()))
    
    # Check if path exists
    path_exists, path_length = check_path_exists_matrix(adjacency_matrix, path_sequence)
    
    # Print the result
    if path_exists:
        print(f"Path exists with sequence: {path_sequence}")
        print(f"Length of the path: {path_length}")
    else:
        print(f"Path does NOT exist with sequence: {path_sequence}")


if __name__ == "__main__":
    main()
