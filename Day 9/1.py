import heapq
import matplotlib.pyplot as plt
import numpy as np
import time

# Manhattan Distance
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_visual(grid, start, goal):
    rows, cols = len(grid), len(grid[0])

    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {start: 0}

    visited = set()

    while open_set:
        current = heapq.heappop(open_set)[1]
        visited.add(current)

        draw_grid(grid, start, goal, visited, current)
        time.sleep(0.2)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        x, y = current
        neighbors = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                tentative_g = g_score[current] + 1

                if (nx, ny) not in g_score or tentative_g < g_score[(nx, ny)]:
                    came_from[(nx, ny)] = current
                    g_score[(nx, ny)] = tentative_g
                    f_score = tentative_g + heuristic((nx, ny), goal)
                    heapq.heappush(open_set, (f_score, (nx, ny)))

    return None


def draw_grid(grid, start, goal, visited, current, path=None):
    plt.clf()
    grid_np = np.array(grid)

    plt.imshow(grid_np, cmap="gray_r")

    # visited nodes
    for v in visited:
        plt.scatter(v[1], v[0])

    # current node
    plt.scatter(current[1], current[0])

    # path
    if path:
        px, py = zip(*path)
        plt.plot(py, px)

    # start and goal
    plt.scatter(start[1], start[0])
    plt.scatter(goal[1], goal[0])

    plt.pause(0.01)


# -------- USER INPUT --------

rows = int(input("Enter rows: "))
cols = int(input("Enter cols: "))

grid = []
print("Enter grid (0 = free, 1 = obstacle):")
for _ in range(rows):
    grid.append(list(map(int, input().split())))

start = tuple(map(int, input("Enter start (row col): ").split()))
goal = tuple(map(int, input("Enter goal (row col): ").split()))

plt.figure(figsize=(6,6))

path = astar_visual(grid, start, goal)

if path:
    print("Path Found!")
    draw_grid(grid, start, goal, set(), goal, path)
    plt.show()
else:
    print("No Path Found")
