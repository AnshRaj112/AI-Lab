"""
Write a program to check if there exists a path with the given sequence of nodes.
If yes, find out the length of the path.
(input-adjacency list, user fed list)
"""

from graph_utils import get_adjacency_list_input, display_adjacency_list, check_path_exists_list


def main():
    """Main function to check if a path exists with given sequence of nodes."""
    # Take input from the user
    adjacency_list = get_adjacency_list_input()
    
    # Print the adjacency list
    display_adjacency_list(adjacency_list)
    
    # Get the sequence of nodes
    path_sequence = list(map(int, input("Enter the sequence of nodes (space-separated): ").split()))
    
    # Check if path exists
    path_exists, path_length = check_path_exists_list(adjacency_list, path_sequence)
    
    # Print the result
    if path_exists:
        print(f"Path exists with sequence: {path_sequence}")
        print(f"Length of the path: {path_length}")
    else:
        print(f"Path does NOT exist with sequence: {path_sequence}")


if __name__ == "__main__":
    main()
