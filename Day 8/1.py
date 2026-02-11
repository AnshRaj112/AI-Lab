import heapq
import time


# -------- HEURISTIC FUNCTION --------
def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


# -------- GRID VISUALIZATION --------
def print_grid(grid, path=None, start=None, goal=None):
    for i in range(len(grid)):
        row = ""
        for j in range(len(grid[0])):
            if (i, j) == start:
                row += " S "
            elif (i, j) == goal:
                row += " T "
            elif path and (i, j) in path:
                row += " * "
            elif grid[i][j] == 1:
                row += " # "
            else:
                row += " . "
        print(row)
    print("\n")


# -------- GREEDY BEST-FIRST SEARCH (GBFS) --------
def greedy_best_first_search(grid, start, goal):

    pq = []
    heapq.heappush(pq, (manhattan(start, goal), start))

    visited = set()
    parent = {}

    while pq:
        h, current = heapq.heappop(pq)

        if current == goal:
            break

        if current in visited:
            continue

        visited.add(current)

        x, y = current
        neighbors = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

        for nx, ny in neighbors:
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == 0 and (nx, ny) not in visited:
                    heapq.heappush(pq, (manhattan((nx, ny), goal), (nx, ny)))
                    parent[(nx, ny)] = current

    # Path reconstruction
    path = []
    node = goal

    while node != start:
        path.append(node)
        node = parent.get(node, start)

    path.append(start)
    path.reverse()

    return path


# -------- A* SEARCH ALGORITHM --------
def a_star_search(grid, start, goal):

    pq = []
    heapq.heappush(pq, (0, start))

    g_cost = {start: 0}
    parent = {}

    while pq:
        f, current = heapq.heappop(pq)

        if current == goal:
            break

        x, y = current
        neighbors = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

        for nx, ny in neighbors:
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                if grid[nx][ny] == 0:

                    new_cost = g_cost[current] + 1

                    if (nx, ny) not in g_cost or new_cost < g_cost[(nx, ny)]:
                        g_cost[(nx, ny)] = new_cost
                        f = new_cost + manhattan((nx, ny), goal)
                        heapq.heappush(pq, (f, (nx, ny)))
                        parent[(nx, ny)] = current

    # Path reconstruction
    path = []
    node = goal

    while node != start:
        path.append(node)
        node = parent.get(node, start)

    path.append(start)
    path.reverse()

    return path


# -------- TAKING USER INPUT --------
def get_user_grid():

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    grid = [[0 for _ in range(cols)] for _ in range(rows)]

    print("\nEnter number of obstacles:")
    obs = int(input())

    print("\nEnter obstacle positions as: row col")

    for _ in range(obs):
        x, y = map(int, input().split())
        grid[x][y] = 1

    print("\nEnter Start position (row col):")
    sx, sy = map(int, input().split())
    start = (sx, sy)

    print("\nEnter Goal position (row col):")
    gx, gy = map(int, input().split())
    goal = (gx, gy)

    return grid, start, goal


# -------- MAIN DRIVER --------
if __name__ == "__main__":

    print("----- GREEDY BEST-FIRST SEARCH vs A* SEARCH -----\n")

    grid, start, goal = get_user_grid()

    print("\nINITIAL GRID:")
    print_grid(grid, start=start, goal=goal)

    print("Choose Algorithm:")
    print("1. Greedy Best-First Search (GBFS)")
    print("2. A* Search")
    print("3. Compare Both")

    choice = int(input("\nEnter choice (1/2/3): "))

    if choice == 1:
        print("\nRunning Greedy Best-First Search...\n")
        t1 = time.time()
        path = greedy_best_first_search(grid, start, goal)
        t2 = time.time()

        print_grid(grid, path=path, start=start, goal=goal)
        print("Path Length:", len(path))
        print("Time Taken:", round(t2 - t1, 5), "seconds")

    elif choice == 2:
        print("\nRunning A* Search...\n")
        t1 = time.time()
        path = a_star_search(grid, start, goal)
        t2 = time.time()

        print_grid(grid, path=path, start=start, goal=goal)
        print("Path Length:", len(path))
        print("Time Taken:", round(t2 - t1, 5), "seconds")

    elif choice == 3:

        print("\nRunning Greedy Best-First Search...\n")
        t1 = time.time()
        gbfs_path = greedy_best_first_search(grid, start, goal)
        t2 = time.time()

        print("Running A* Search...\n")
        t3 = time.time()
        astar_path = a_star_search(grid, start, goal)
        t4 = time.time()

        print("GBFS Result:")
        print_grid(grid, path=gbfs_path, start=start, goal=goal)

        print("A* Result:")
        print_grid(grid, path=astar_path, start=start, goal=goal)

        print("----- COMPARISON -----")
        print("GBFS Path Length:", len(gbfs_path))
        print("A* Path Length:", len(astar_path))
        print("GBFS Time:", round(t2 - t1, 5))
        print("A* Time:", round(t4 - t3, 5))

        if len(astar_path) <= len(gbfs_path):
            print("\nA* produced a better or equal optimal path.")
        else:
            print("\nGBFS got lucky this time!")

    else:
        print("Invalid Choice!")
