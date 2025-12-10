"""
Write a program to calculate the degree of each vertex in an undirected graph.(input-adjacency list, output degree of each vertex, user fed list)
"""

from graph_utils import get_adjacency_list_input, display_adjacency_list, calculate_degrees_from_list


def main():
    """Main function to calculate the degree of each vertex."""
    # Take input from the user
    adjacency_list = get_adjacency_list_input()
    
    # Print the adjacency list
    display_adjacency_list(adjacency_list)
    
    # Print the degree of each vertex
    print(f"Degrees: {calculate_degrees_from_list(adjacency_list)}")


if __name__ == "__main__":
    main()
