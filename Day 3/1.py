"""
Write a program to create a list and perform insert, delete, and search operations.
"""


def insert_element(lst, index, value):
    """Insert an element at a specific index in the list."""
    lst.insert(index, value)
    return lst


def delete_element(lst, value):
    """Delete the first occurrence of an element from the list."""
    if value in lst:
        lst.remove(value)
        return True, lst
    return False, lst


def delete_by_index(lst, index):
    """Delete an element at a specific index."""
    if 0 <= index < len(lst):
        deleted_value = lst.pop(index)
        return deleted_value, lst
    return None, lst


def search_element(lst, value):
    """Search for an element in the list and return its index."""
    if value in lst:
        return lst.index(value)
    return -1


def display_menu():
    """Display the menu options."""
    print("\n" + "="*50)
    print("LIST OPERATIONS MENU")
    print("="*50)
    print("1. Insert element at index")
    print("2. Delete element by value")
    print("3. Delete element by index")
    print("4. Search element")
    print("5. Display list")
    print("6. Exit")
    print("="*50)


def main():
    """Main function to perform list operations."""
    # Initialize the list
    print("Enter initial list elements (space-separated):")
    user_input = input().strip()
    if user_input:
        my_list = [int(x) if x.isdigit() or (x[0] == '-' and x[1:].isdigit()) else x for x in user_input.split()]
    else:
        my_list = []
    
    print(f"\nInitial list: {my_list}")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            try:
                index = int(input("Enter index to insert at: "))
                value = input("Enter value to insert: ")
                # Try to convert to int if possible
                try:
                    value = int(value)
                except ValueError:
                    try:
                        value = float(value)
                    except ValueError:
                        pass  # Keep as string
                
                my_list = insert_element(my_list, index, value)
                print(f"Element inserted successfully!")
                print(f"Updated list: {my_list}")
            except ValueError:
                print("Invalid input! Please enter a valid integer for index.")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == '2':
            value = input("Enter value to delete: ")
            # Try to convert to int if possible
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass  # Keep as string
            
            found, my_list = delete_element(my_list, value)
            if found:
                print(f"Element '{value}' deleted successfully!")
                print(f"Updated list: {my_list}")
            else:
                print(f"Element '{value}' not found in the list!")
        
        elif choice == '3':
            try:
                index = int(input("Enter index to delete: "))
                deleted_value, my_list = delete_by_index(my_list, index)
                if deleted_value is not None:
                    print(f"Element at index {index} ({deleted_value}) deleted successfully!")
                    print(f"Updated list: {my_list}")
                else:
                    print("Invalid index! Index out of range.")
            except ValueError:
                print("Invalid input! Please enter a valid integer for index.")
        
        elif choice == '4':
            value = input("Enter value to search: ")
            # Try to convert to int if possible
            try:
                value = int(value)
            except ValueError:
                try:
                    value = float(value)
                except ValueError:
                    pass  # Keep as string
            
            index = search_element(my_list, value)
            if index != -1:
                print(f"Element '{value}' found at index: {index}")
            else:
                print(f"Element '{value}' not found in the list!")
        
        elif choice == '5':
            print(f"Current list: {my_list}")
            print(f"List length: {len(my_list)}")
        
        elif choice == '6':
            print("Exiting program. Final list:", my_list)
            break
        
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()

