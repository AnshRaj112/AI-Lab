"""
write a function oriented program to calculate the number of edges in an undirected graph.(input-adjacency list, output number of edges, user fed list)
"""

from graph_utils import get_adjacency_list_input, display_adjacency_list, count_edges_from_list


def main():
    """Main function to calculate the number of edges."""
    # Take input from the user
    adjacency_list = get_adjacency_list_input()
    
    # Print the adjacency list
    display_adjacency_list(adjacency_list)
    
    # Print the number of edges
    print(f"Number of edges: {count_edges_from_list(adjacency_list)}")


if __name__ == "__main__":
    main()