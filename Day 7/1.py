import heapq
from copy import deepcopy

# -------------------------------
# 8-Puzzle State Representation
# -------------------------------
class PuzzleState:
    def __init__(self, board, parent=None, move=None, g_cost=0):
        """
        Initialize a puzzle state.
        board: 3x3 list representing the puzzle state (0 represents empty tile)
        parent: Parent state in the search tree
        move: The move that led to this state
        g_cost: Cost from start to this state
        """
        self.board = board
        self.parent = parent
        self.move = move
        self.g_cost = g_cost
        self.blank_pos = self._find_blank()
    
    def _find_blank(self):
        """Find the position of the blank tile (0)."""
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return (i, j)
        return None
    
    def __eq__(self, other):
        """Check if two states are equal."""
        return self.board == other.board
    
    def __hash__(self):
        """Make state hashable for set operations."""
        return hash(tuple(tuple(row) for row in self.board))
    
    def __lt__(self, other):
        """For priority queue ordering (tie-breaker)."""
        return self.g_cost < other.g_cost
    
    def get_successors(self):
        """Generate all possible successor states."""
        successors = []
        i, j = self.blank_pos
        moves = [(-1, 0, 'UP'), (1, 0, 'DOWN'), (0, -1, 'LEFT'), (0, 1, 'RIGHT')]
        
        for di, dj, move_name in moves:
            new_i, new_j = i + di, j + dj
            
            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_board = deepcopy(self.board)
                new_board[i][j], new_board[new_i][new_j] = new_board[new_i][new_j], new_board[i][j]
                successors.append(PuzzleState(new_board, self, move_name, self.g_cost + 1))
        
        return successors
    
    def is_goal(self, goal_state):
        """Check if this state matches the goal state."""
        return self.board == goal_state
    
    def print_state(self):
        """Print the puzzle state in a readable format."""
        for row in self.board:
            print(' '.join(str(tile) if tile != 0 else '_' for tile in row))
        print()


# -------------------------------
# Heuristic Functions
# -------------------------------
def h1_misplaced_tiles(state, goal_state):
    """
    H1: Number of misplaced tiles (excluding blank).
    Returns the count of tiles that are not in their goal positions.
    """
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state.board[i][j] != 0 and state.board[i][j] != goal_state[i][j]:
                misplaced += 1
    return misplaced


def h2_manhattan_distance(state, goal_state):
    """
    H2: Sum of Manhattan distances of all tiles from their goal positions.
    Manhattan distance = |x1 - x2| + |y1 - y2|
    """
    # Create a mapping of tile value to goal position
    goal_positions = {}
    for i in range(3):
        for j in range(3):
            goal_positions[goal_state[i][j]] = (i, j)
    
    total_distance = 0
    for i in range(3):
        for j in range(3):
            tile = state.board[i][j]
            if tile != 0:  # Don't count blank tile
                goal_i, goal_j = goal_positions[tile]
                total_distance += abs(i - goal_i) + abs(j - goal_j)
    
    return total_distance


# -------------------------------
# A* Search Algorithm
# -------------------------------
def a_star_search(initial_state, goal_state, heuristic_func):
    """
    A* search algorithm for solving 8-puzzle.
    
    Args:
        initial_state: Starting puzzle state
        goal_state: Goal puzzle configuration (3x3 list)
        heuristic_func: Heuristic function (h1 or h2)
    
    Returns:
        tuple: (solution_path, nodes_explored, solution_depth) or (None, nodes_explored, None)
    """
    # Priority queue: (f_cost, g_cost, state)
    # f_cost = g_cost + h_cost
    priority_queue = [(0, 0, initial_state)]
    visited = set()
    nodes_explored = 0
    
    while priority_queue:
        f_cost, g_cost, current_state = heapq.heappop(priority_queue)
        
        # Skip if already visited
        if current_state in visited:
            continue
        
        visited.add(current_state)
        nodes_explored += 1
        
        # Check if goal is reached
        if current_state.is_goal(goal_state):
            # Reconstruct path using parent pointers
            path = []
            state = current_state
            while state is not None:
                path.append(state)
                state = state.parent
            path.reverse()
            
            solution_depth = len(path) - 1
            return path, nodes_explored, solution_depth
        
        # Generate successors
        for successor in current_state.get_successors():
            if successor not in visited:
                h_cost = heuristic_func(successor, goal_state)
                f_cost = successor.g_cost + h_cost
                heapq.heappush(priority_queue, (f_cost, successor.g_cost, successor))
    
    return None, nodes_explored, None


# -------------------------------
# Performance Comparison
# -------------------------------
def compare_heuristics(initial_state, goal_state):
    """
    Compare the performance of H1 and H2 heuristics.
    """
    print("=" * 60)
    print("COMPARING HEURISTICS FOR 8-PUZZLE")
    print("=" * 60)
    
    # Test with H1 (Misplaced Tiles)
    print("\n[1] Running A* with H1 (Misplaced Tiles)...")
    path_h1, nodes_h1, depth_h1 = a_star_search(initial_state, goal_state, h1_misplaced_tiles)
    
    # Test with H2 (Manhattan Distance)
    print("[2] Running A* with H2 (Manhattan Distance)...")
    path_h2, nodes_h2, depth_h2 = a_star_search(initial_state, goal_state, h2_manhattan_distance)
    
    # Display Results
    print("\n" + "=" * 60)
    print("RESULTS")
    print("=" * 60)
    
    print("\n--- H1 (Misplaced Tiles) ---")
    if path_h1:
        print(f"Solution Found: YES")
        print(f"Solution Depth: {depth_h1} moves")
        print(f"Nodes Explored: {nodes_h1}")
        print(f"\nSolution Path ({len(path_h1)} states):")
        for i, state in enumerate(path_h1):
            print(f"\nStep {i}: {state.move if state.move else 'INITIAL'}")
            state.print_state()
    else:
        print("Solution Found: NO")
        print(f"Nodes Explored: {nodes_h1}")
    
    print("\n--- H2 (Manhattan Distance) ---")
    if path_h2:
        print(f"Solution Found: YES")
        print(f"Solution Depth: {depth_h2} moves")
        print(f"Nodes Explored: {nodes_h2}")
        print(f"\nSolution Path ({len(path_h2)} states):")
        for i, state in enumerate(path_h2):
            print(f"\nStep {i}: {state.move if state.move else 'INITIAL'}")
            state.print_state()
    else:
        print("Solution Found: NO")
        print(f"Nodes Explored: {nodes_h2}")
    
    # Comparison Summary
    print("\n" + "=" * 60)
    print("COMPARISON SUMMARY")
    print("=" * 60)
    
    if path_h1 and path_h2:
        print(f"\n{'Metric':<25} {'H1 (Misplaced)':<20} {'H2 (Manhattan)':<20}")
        print("-" * 65)
        print(f"{'Nodes Explored':<25} {nodes_h1:<20} {nodes_h2:<20}")
        print(f"{'Solution Depth':<25} {depth_h1:<20} {depth_h2:<20}")
        
        efficiency_h1 = nodes_h1 / depth_h1 if depth_h1 > 0 else float('inf')
        efficiency_h2 = nodes_h2 / depth_h2 if depth_h2 > 0 else float('inf')
        print(f"{'Nodes/Depth Ratio':<25} {efficiency_h1:<20.2f} {efficiency_h2:<20.2f}")
        
        print(f"\n{'Winner':<25} {'H1' if nodes_h1 < nodes_h2 else 'H2' if nodes_h2 < nodes_h1 else 'TIE'}")
        if nodes_h1 < nodes_h2:
            print(f"  → H1 explored {nodes_h2 - nodes_h1} fewer nodes")
        elif nodes_h2 < nodes_h1:
            print(f"  → H2 explored {nodes_h1 - nodes_h2} fewer nodes")
        else:
            print(f"  → Both heuristics performed equally")
    else:
        print("\nCould not complete comparison (one or both searches failed)")


# -------------------------------
# Input Functions
# -------------------------------
def get_puzzle_input(prompt):
    """Get 3x3 puzzle state from user."""
    print(prompt)
    print("Enter 9 numbers (0-8) representing the puzzle state row by row.")
    print("Use 0 for the blank tile. Enter 3 numbers per line:")
    
    board = []
    for i in range(3):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        if len(row) != 3:
            raise ValueError("Each row must have exactly 3 numbers")
        board.append(row)
    
    return board


def get_puzzle_input_simple():
    """Get puzzle input in a simpler format (single line)."""
    print("Enter 9 numbers (0-8) separated by spaces (0 = blank):")
    print("Example: 1 2 3 4 5 6 7 8 0")
    numbers = list(map(int, input().split()))
    
    if len(numbers) != 9:
        raise ValueError("Must enter exactly 9 numbers")
    
    board = [numbers[i:i+3] for i in range(0, 9, 3)]
    return board


# -------------------------------
# Main Execution
# -------------------------------
def main():
    print("=" * 60)
    print("8-PUZZLE SOLVER USING A* SEARCH")
    print("=" * 60)
    
    # Default goal state (standard 8-puzzle goal)
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    
    print("\nGoal State:")
    for row in goal_state:
        print(' '.join(str(tile) if tile != 0 else '_' for tile in row))
    
    print("\n" + "-" * 60)
    print("Choose input method:")
    print("1. Enter puzzle state row by row (3 lines)")
    print("2. Enter puzzle state in single line (9 numbers)")
    choice = input("Enter choice (1 or 2): ").strip()
    
    try:
        if choice == "1":
            initial_board = get_puzzle_input("\nEnter Initial State:")
        else:
            initial_board = get_puzzle_input_simple()
        
        initial_state = PuzzleState(initial_board)
        
        print("\nInitial State:")
        initial_state.print_state()
        
        # Run comparison
        compare_heuristics(initial_state, goal_state)
        
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nUnexpected error: {e}")


# -------------------------------
# Test with Example
# -------------------------------
def test_example():
    """Test with a predefined example."""
    print("=" * 60)
    print("TESTING WITH EXAMPLE PUZZLE")
    print("=" * 60)
    
    # Example: Solvable puzzle
    initial_board = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
    goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    
    initial_state = PuzzleState(initial_board)
    
    print("\nInitial State:")
    initial_state.print_state()
    
    print("Goal State:")
    for row in goal_state:
        print(' '.join(str(tile) if tile != 0 else '_' for tile in row))
    print()
    
    compare_heuristics(initial_state, goal_state)


if __name__ == "__main__":
    # Uncomment the line below to run with a test example
    # test_example()
    
    # Run interactive mode
    main()

