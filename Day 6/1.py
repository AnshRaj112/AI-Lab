import heapq
from collections import deque

# -------------------------------
# Uniform Cost Search Algorithm
# -------------------------------
def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start, [start])]  # (cost, current_node, path)
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue

        visited.add(node)

        if node == goal:
            return path, cost

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(
                    priority_queue,
                    (cost + weight, neighbor, path + [neighbor])
                )

    return None, float('inf')


# -------------------------------
# Breadth First Search Algorithm
# (For comparison – unweighted)
# -------------------------------
def bfs(graph, start, goal):
    queue = deque([(start, [start])])
    visited = set([start])

    while queue:
        node, path = queue.popleft()

        if node == goal:
            return path

        for neighbor, _ in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None


# -------------------------------
# Taking Graph Input from User
# -------------------------------
def take_graph_input():
    graph = {}
    edges = int(input("Enter number of edges: "))

    print("\nEnter edges in format: source destination cost")
    for _ in range(edges):
        src, dest, cost = input().split()
        cost = int(cost)

        if src not in graph:
            graph[src] = []

        graph[src].append((dest, cost))

    return graph


# -------------------------------
# Main Execution
# -------------------------------
def main():
    graph = take_graph_input()

    start = input("\nEnter start node: ")
    goal = input("Enter goal node: ")

    ucs_path, ucs_cost = uniform_cost_search(graph, start, goal)
    bfs_path = bfs(graph, start, goal)

    print("\n========== RESULTS ==========")

    if ucs_path:
        print("Uniform Cost Search Path :", ucs_path)
        print("Total Cost               :", ucs_cost)
    else:
        print("No path found using UCS")

    if bfs_path:
        print("BFS Path (ignores cost)  :", bfs_path)
    else:
        print("No path found using BFS")


if __name__ == "__main__":
    main()
