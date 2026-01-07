from collections import deque

# -------------------------------
# Utility: Get valid neighbors
# -------------------------------
def get_neighbors(maze, cell):
    neighbors = []
    rows, cols = len(maze), len(maze[0])
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    for dr, dc in directions:
        r, c = cell[0] + dr, cell[1] + dc
        if 0 <= r < rows and 0 <= c < cols and maze[r][c] == 1:
            neighbors.append((r, c))

    return neighbors


# -------------------------------
# BFS: Shortest Path
# -------------------------------
def bfs(maze, start, end):
    queue = deque([(start, [start])])
    visited = set([start])
    nodes_explored = 0

    while queue:
        current, path = queue.popleft()
        nodes_explored += 1

        if current == end:
            return path, nodes_explored

        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))

    return None, nodes_explored


# -------------------------------
# DFS: Any Valid Path
# -------------------------------
def dfs(maze, start, end):
    stack = [(start, [start])]
    visited = set([start])
    nodes_explored = 0

    while stack:
        current, path = stack.pop()
        nodes_explored += 1

        if current == end:
            return path, nodes_explored

        for neighbor in get_neighbors(maze, current):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append((neighbor, path + [neighbor]))

    return None, nodes_explored


# -------------------------------
# Visual Maze Printing
# -------------------------------
def print_maze(maze, path=None, start=None, end=None):
    print("\nMaze Visualization:")
    print("█ = Wall | · = Path | S = Start | E = End | * = Solution Path\n")

    path = set(path) if path else set()

    for i in range(len(maze)):
        for j in range(len(maze[0])):
            cell = (i, j)
            if cell == start:
                print("S", end=" ")
            elif cell == end:
                print("E", end=" ")
            elif cell in path:
                print("*", end=" ")
            elif maze[i][j] == 1:
                print("·", end=" ")
            else:
                print("█", end=" ")
        print()
    print()


# -------------------------------
# Manual Maze Input
# -------------------------------
def get_maze_input():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("\nEnter maze row by row (0 = wall, 1 = path):")
    maze = []

    for i in range(rows):
        while True:
            row = list(map(int, input(f"Row {i+1}: ").split()))
            if len(row) == cols and all(cell in (0,1) for cell in row):
                maze.append(row)
                break
            else:
                print("Invalid row. Try again.")

    return maze


# -------------------------------
# Main Program
# -------------------------------
def main():
    print("=" * 50)
    print("MAZE SOLVER USING BFS & DFS")
    print("=" * 50)

    print("\nChoose input method:")
    print("1. Manual maze entry")
    print("2. Use default maze")

    choice = input("\nEnter choice (1 or 2): ").strip()

    if choice == '1':
        maze = get_maze_input()
    else:
        maze = [
            [1, 0, 1, 1, 1],
            [1, 1, 1, 0, 1],
            [0, 1, 0, 1, 1],
            [1, 1, 1, 1, 0],
            [1, 0, 1, 1, 1],
        ]

    rows, cols = len(maze), len(maze[0])

    try:
        start = tuple(map(int, input("\nEnter start cell (row col): ").split()))
        end = tuple(map(int, input("Enter end cell (row col): ").split()))

        if not (0 <= start[0] < rows and 0 <= start[1] < cols):
            raise ValueError
        if not (0 <= end[0] < rows and 0 <= end[1] < cols):
            raise ValueError
        if maze[start[0]][start[1]] == 0 or maze[end[0]][end[1]] == 0:
            raise ValueError

    except ValueError:
        print("\nInvalid input. Using default start (0,0) and end (4,4).")
        start = (0, 0)
        end = (rows-1, cols-1)

    print_maze(maze, start=start, end=end)

    # BFS
    bfs_path, bfs_nodes = bfs(maze, start, end)
    if bfs_path:
        print("BFS Result:")
        print(f"Shortest Path: {bfs_path}")
        print(f"Nodes Explored: {bfs_nodes}")
        print_maze(maze, bfs_path, start, end)
    else:
        print("No path found using BFS.")

    # DFS
    dfs_path, dfs_nodes = dfs(maze, start, end)
    if dfs_path:
        print("DFS Result:")
        print(f"Valid Path: {dfs_path}")
        print(f"Nodes Explored: {dfs_nodes}")
        print_maze(maze, dfs_path, start, end)
    else:
        print("No path found using DFS.")

    print("=" * 50)


if __name__ == "__main__":
    main()
