"""
Write a program to check whether a key exists in a dictionary.
"""


def check_key_exists(dictionary, key):
    """Check if a key exists in the dictionary."""
    return key in dictionary


def check_key_get_value(dictionary, key):
    """Check if key exists and return its value, None otherwise."""
    return dictionary.get(key)


def check_key_get_default(dictionary, key, default="Key not found"):
    """Check if key exists and return its value, default otherwise."""
    return dictionary.get(key, default)


def main():
    """Main function to check key existence in dictionary."""
    print("="*50)
    print("CHECK KEY EXISTS IN DICTIONARY")
    print("="*50)
    print("\nChoose input method:")
    print("1. Manual entry (interactive)")
    print("2. Use default dictionary")
    
    choice = input("\nEnter choice (1 or 2): ").strip()
    
    if choice == '1':
        my_dict = {}
        print("\nEnter key-value pairs (press Enter with empty key to finish):")
        
        while True:
            key = input("\nEnter key (or press Enter to finish): ").strip()
            if not key:
                break
            
            value = input(f"Enter value for '{key}': ").strip()
            
            # Try to convert value to appropriate type
            if value.lower() == 'true':
                value = True
            elif value.lower() == 'false':
                value = False
            elif value.lower() == 'none' or value == '':
                value = None
            else:
                try:
                    value = int(value)
                except ValueError:
                    try:
                        value = float(value)
                    except ValueError:
                        pass
            
            my_dict[key] = value
            print(f"Added: {key} = {value}")
    
    else:
        # Default dictionary
        print("\nUsing default dictionary...")
        my_dict = {
            'name': 'Alice',
            'age': 25,
            'city': 'London',
            'salary': 45000,
            'is_active': True,
            'department': 'Engineering'
        }
    
    # Display dictionary
    print("\n" + "="*50)
    print("DICTIONARY")
    print("="*50)
    print(f"Dictionary: {my_dict}")
    print(f"Available keys: {list(my_dict.keys())}")
    
    # Check for keys
    print("\n" + "="*50)
    print("KEY CHECK OPERATIONS")
    print("="*50)
    
    while True:
        key_to_check = input("\nEnter a key to check (or 'quit' to exit): ").strip()
        
        if key_to_check.lower() == 'quit':
            break
        
        if not key_to_check:
            print("Please enter a valid key!")
            continue
        
        # Method 1: Using 'in' operator
        exists1 = check_key_exists(my_dict, key_to_check)
        print(f"\nMethod 1 (using 'in' operator):")
        print(f"  Key '{key_to_check}' exists: {exists1}")
        
        # Method 2: Using .get() method
        value2 = check_key_get_value(my_dict, key_to_check)
        print(f"\nMethod 2 (using .get() method):")
        if value2 is not None:
            print(f"  Key '{key_to_check}' exists with value: {value2}")
        else:
            print(f"  Key '{key_to_check}' does not exist")
        
        # Method 3: Using .get() with default
        value3 = check_key_get_default(my_dict, key_to_check, "NOT FOUND")
        print(f"\nMethod 3 (using .get() with default):")
        print(f"  Value for '{key_to_check}': {value3}")
        
        # Method 4: Using try-except
        try:
            value4 = my_dict[key_to_check]
            print(f"\nMethod 4 (using try-except):")
            print(f"  Key '{key_to_check}' exists with value: {value4}")
        except KeyError:
            print(f"\nMethod 4 (using try-except):")
            print(f"  Key '{key_to_check}' does not exist (KeyError raised)")
        
        print("\n" + "-"*50)


if __name__ == "__main__":
    main()

