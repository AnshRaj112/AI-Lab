"""
Write a program to swap two elements in a list using indices.
"""


def swap_elements(lst, index1, index2):
    """Swap two elements in a list using their indices."""
    # Validate indices
    if index1 < 0 or index1 >= len(lst):
        raise IndexError(f"Index {index1} is out of range!")
    if index2 < 0 or index2 >= len(lst):
        raise IndexError(f"Index {index2} is out of range!")
    
    # Swap elements
    lst[index1], lst[index2] = lst[index2], lst[index1]
    return lst


def main():
    """Main function to swap elements in a list."""
    print("="*50)
    print("SWAP ELEMENTS IN LIST")
    print("="*50)
    print("\nEnter list elements (space-separated):")
    user_input = input().strip()
    
    if not user_input:
        print("No input provided. Using default list: [10, 20, 30, 40, 50]")
        my_list = [10, 20, 30, 40, 50]
    else:
        # Try to convert to appropriate types
        elements = user_input.split()
        my_list = []
        for elem in elements:
            try:
                # Try int first
                my_list.append(int(elem))
            except ValueError:
                try:
                    # Try float
                    my_list.append(float(elem))
                except ValueError:
                    # Keep as string
                    my_list.append(elem)
    
    print(f"\nOriginal list: {my_list}")
    print(f"List length: {len(my_list)}")
    
    if len(my_list) == 0:
        print("Error: List is empty! Cannot swap elements.")
        return
    
    # Get indices from user
    try:
        print("\nEnter two indices to swap:")
        index1 = int(input("Index 1: "))
        index2 = int(input("Index 2: "))
        
        # Store original values for display
        value1 = my_list[index1]
        value2 = my_list[index2]
        
        # Perform swap
        my_list = swap_elements(my_list, index1, index2)
        
        # Display results
        print(f"\nSwapped elements at indices {index1} and {index2}")
        print(f"  Index {index1}: {value1} -> {my_list[index1]}")
        print(f"  Index {index2}: {value2} -> {my_list[index2]}")
        print(f"\nUpdated list: {my_list}")
        
    except ValueError:
        print("Error: Please enter valid integer indices!")
    except IndexError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()

