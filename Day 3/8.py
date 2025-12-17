"""
Represent a 2D grid using a list of lists.
- Print all valid neighbors (up, down, left, right) of a cell
- Check if a cell is inside the grid boundary
- Count the number of obstacles
"""


def is_valid_cell(grid, row, col):
    """Check if a cell (row, col) is inside the grid boundary."""
    rows = len(grid)
    if rows == 0:
        return False
    cols = len(grid[0])
    return 0 <= row < rows and 0 <= col < cols


def get_neighbors(grid, row, col):
    """Get all valid neighbors (up, down, left, right) of a cell."""
    neighbors = []
    directions = [
        ('Up', -1, 0),
        ('Down', 1, 0),
        ('Left', 0, -1),
        ('Right', 0, 1)
    ]
    
    for direction, dr, dc in directions:
        new_row = row + dr
        new_col = col + dc
        
        if is_valid_cell(grid, new_row, new_col):
            neighbors.append({
                'direction': direction,
                'position': (new_row, new_col),
                'value': grid[new_row][new_col]
            })
    
    return neighbors


def count_obstacles(grid, obstacle_value=0):
    """
    Count the number of obstacles in the grid.
    By default, obstacles are cells with value 0.
    """
    count = 0
    for row in grid:
        for cell in row:
            if cell == obstacle_value:
                count += 1
    return count


def display_grid(grid):
    """Display the grid in a formatted way."""
    print("\n" + "="*50)
    print("2D GRID")
    print("="*50)
    rows = len(grid)
    if rows == 0:
        print("Empty grid!")
        return
    
    cols = len(grid[0])
    print(f"Grid dimensions: {rows} x {cols}")
    print("\nGrid layout:")
    print("   ", end="")
    for j in range(cols):
        print(f"{j:4}", end="")
    print()
    
    for i in range(rows):
        print(f"{i:2} ", end="")
        for j in range(cols):
            print(f"{str(grid[i][j]):4}", end="")
        print()
    print("="*50)


def main():
    """Main function for 2D grid operations."""
    print("="*50)
    print("2D GRID OPERATIONS")
    print("="*50)
    print("\nChoose input method:")
    print("1. Manual entry (interactive)")
    print("2. Use default grid")
    
    choice = input("\nEnter choice (1 or 2): ").strip()
    
    if choice == '1':
        print("\nEnter grid dimensions:")
        try:
            rows = int(input("Number of rows: "))
            cols = int(input("Number of columns: "))
            
            if rows <= 0 or cols <= 0:
                print("Invalid dimensions! Using default grid.")
                grid = [
                    [1, 0, 1, 1],
                    [1, 1, 0, 1],
                    [0, 1, 1, 1],
                    [1, 1, 1, 0]
                ]
            else:
                grid = []
                print(f"\nEnter {rows} rows, each with {cols} space-separated values:")
                for i in range(rows):
                    row_input = input(f"Row {i}: ").strip().split()
                    if len(row_input) != cols:
                        print(f"Warning: Expected {cols} values, got {len(row_input)}. Padding with 0s.")
                        row_input = (row_input + [0] * cols)[:cols]
                    
                    row = []
                    for val in row_input:
                        try:
                            row.append(int(val))
                        except ValueError:
                            try:
                                row.append(float(val))
                            except ValueError:
                                row.append(val)
                    grid.append(row)
        
        except ValueError:
            print("Invalid input! Using default grid.")
            grid = [
                [1, 0, 1, 1],
                [1, 1, 0, 1],
                [0, 1, 1, 1],
                [1, 1, 1, 0]
            ]
    
    else:
        # Default grid (1 = free, 0 = obstacle)
        print("\nUsing default grid (1 = free, 0 = obstacle)...")
        grid = [
            [1, 0, 1, 1],
            [1, 1, 0, 1],
            [0, 1, 1, 1],
            [1, 1, 1, 0]
        ]
    
    # Display grid
    display_grid(grid)
    
    # Count obstacles
    obstacle_count = count_obstacles(grid, obstacle_value=0)
    print(f"\nNumber of obstacles (cells with value 0): {obstacle_count}")
    
    # Interactive cell operations
    print("\n" + "="*50)
    print("CELL OPERATIONS")
    print("="*50)
    
    while True:
        try:
            print("\nEnter cell coordinates (or 'quit' to exit):")
            row_input = input("Row: ").strip()
            
            if row_input.lower() == 'quit':
                break
            
            row = int(row_input)
            col = int(input("Column: ").strip())
            
            print(f"\n" + "-"*50)
            print(f"Operations for cell ({row}, {col}):")
            print("-"*50)
            
            # Check if cell is valid
            is_valid = is_valid_cell(grid, row, col)
            print(f"\n1. Is cell ({row}, {col}) inside grid boundary? {is_valid}")
            
            if is_valid:
                print(f"   Cell value: {grid[row][col]}")
                
                # Get neighbors
                neighbors = get_neighbors(grid, row, col)
                print(f"\n2. Valid neighbors (up, down, left, right):")
                if neighbors:
                    print(f"   Total valid neighbors: {len(neighbors)}")
                    for neighbor in neighbors:
                        dir_name = neighbor['direction']
                        pos = neighbor['position']
                        val = neighbor['value']
                        print(f"   {dir_name:6} -> ({pos[0]}, {pos[1]}) = {val}")
                else:
                    print("   No valid neighbors found.")
            else:
                print(f"   Error: Cell ({row}, {col}) is outside the grid boundary!")
                print(f"   Grid dimensions: {len(grid)} x {len(grid[0]) if grid else 0}")
                print(f"   Valid range: row [0, {len(grid)-1}], col [0, {len(grid[0])-1 if grid else 0}]")
            
            print("-"*50)
        
        except ValueError:
            print("Error: Please enter valid integer coordinates!")
        except Exception as e:
            print(f"Error: {e}")
    
    print("\nProgram ended.")


if __name__ == "__main__":
    main()

