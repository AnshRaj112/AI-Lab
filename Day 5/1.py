from collections import deque

class WaterJugProblem:
    def __init__(self, jug_a_capacity, jug_b_capacity, goal_state):
        self.jug_a_capacity = jug_a_capacity
        self.jug_b_capacity = jug_b_capacity
        self.goal_state = goal_state
    
    def get_next_states(self, state):
        """Generate all possible next states with actions from current state"""
        a, b = state
        next_states = []
        
        # 1. Fill Jug A completely
        if a < self.jug_a_capacity:
            next_states.append(((self.jug_a_capacity, b), "Fill A"))
        
        # 2. Fill Jug B completely
        if b < self.jug_b_capacity:
            next_states.append(((a, self.jug_b_capacity), "Fill B"))
        
        # 3. Empty Jug A
        if a > 0:
            next_states.append(((0, b), "Empty A"))
        
        # 4. Empty Jug B
        if b > 0:
            next_states.append(((a, 0), "Empty B"))
        
        # 5. Pour from Jug A to Jug B
        if a > 0 and b < self.jug_b_capacity:
            space_in_b = self.jug_b_capacity - b
            pour_amount = min(a, space_in_b)
            next_states.append(((a - pour_amount, b + pour_amount), "Pour from A to B"))
        
        # 6. Pour from Jug B to Jug A
        if b > 0 and a < self.jug_a_capacity:
            space_in_a = self.jug_a_capacity - a
            pour_amount = min(b, space_in_a)
            next_states.append(((a + pour_amount, b - pour_amount), "Pour from B to A"))
        
        return next_states
    
    def bfs(self):
        """Breadth-First Search solution"""
        initial_state = (0, 0)
        queue = deque([(initial_state, [(initial_state, "Start")])])
        visited = {initial_state}
        
        print("BFS Solution:")
        print("=" * 50)
        
        while queue:
            current_state, path = queue.popleft()
            
            if current_state == self.goal_state:
                print(f"Goal reached! Path length: {len(path)}")
                print("\nPath:")
                for i, (state, action) in enumerate(path):
                    print(f"Step {i}: {action:20s} → Jug A = {state[0]}L, Jug B = {state[1]}L")
                return path
            
            for next_state, action in self.get_next_states(current_state):
                if next_state not in visited:
                    visited.add(next_state)
                    queue.append((next_state, path + [(next_state, action)]))
        
        print("No solution found!")
        return None
    
    def dfs(self):
        """Depth-First Search solution"""
        initial_state = (0, 0)
        stack = [(initial_state, [(initial_state, "Start")])]
        visited = {initial_state}
        
        print("\nDFS Solution:")
        print("=" * 50)
        
        while stack:
            current_state, path = stack.pop()
            
            if current_state == self.goal_state:
                print(f"Goal reached! Path length: {len(path)}")
                print("\nPath:")
                for i, (state, action) in enumerate(path):
                    print(f"Step {i}: {action:20s} → Jug A = {state[0]}L, Jug B = {state[1]}L")
                return path
            
            # Add next states in reverse order to maintain left-to-right exploration
            next_states = self.get_next_states(current_state)
            for next_state, action in reversed(next_states):
                if next_state not in visited:
                    visited.add(next_state)
                    stack.append((next_state, path + [(next_state, action)]))
        
        print("No solution found!")
        return None
    
    def dfs_recursive(self, current_state, path, visited, max_depth=100):
        """Recursive DFS solution with depth limit"""
        if len(path) > max_depth:
            return None
        
        if current_state == self.goal_state:
            return path
        
        for next_state, action in self.get_next_states(current_state):
            if next_state not in visited:
                visited.add(next_state)
                result = self.dfs_recursive(next_state, path + [(next_state, action)], visited, max_depth)
                if result:
                    return result
                visited.remove(next_state)  # Backtrack
        
        return None


def main():
    # Problem parameters
    jug_a_capacity = 3
    jug_b_capacity = 5
    goal_state = (0, 4)  # Exactly 4 liters in Jug B
    
    problem = WaterJugProblem(jug_a_capacity, jug_b_capacity, goal_state)
    
    # Solve using BFS
    bfs_path = problem.bfs()
    
    # Solve using DFS (iterative)
    dfs_path = problem.dfs()
    
    # Solve using DFS (recursive)
    print("\nDFS (Recursive) Solution:")
    print("=" * 50)
    initial_state = (0, 0)
    visited = {initial_state}
    dfs_recursive_path = problem.dfs_recursive(initial_state, [(initial_state, "Start")], visited)
    
    if dfs_recursive_path:
        print(f"Goal reached! Path length: {len(dfs_recursive_path)}")
        print("\nPath:")
        for i, (state, action) in enumerate(dfs_recursive_path):
            print(f"Step {i}: {action:20s} → Jug A = {state[0]}L, Jug B = {state[1]}L")
    else:
        print("No solution found!")


if __name__ == "__main__":
    main()