"""
Create a dictionary and print all the keys and values.
"""


def print_dict_keys(dictionary):
    """Print all keys in the dictionary."""
    print("\nKeys in the dictionary:")
    for key in dictionary.keys():
        print(f"  - {key}")


def print_dict_values(dictionary):
    """Print all values in the dictionary."""
    print("\nValues in the dictionary:")
    for value in dictionary.values():
        print(f"  - {value}")


def print_dict_items(dictionary):
    """Print all key-value pairs in the dictionary."""
    print("\nKey-Value pairs in the dictionary:")
    for key, value in dictionary.items():
        print(f"  {key}: {value}")


def main():
    """Main function to create and display dictionary."""
    print("="*50)
    print("DICTIONARY KEYS AND VALUES")
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
                    # Try int first
                    value = int(value)
                except ValueError:
                    try:
                        # Try float
                        value = float(value)
                    except ValueError:
                        # Keep as string
                        pass
            
            my_dict[key] = value
            print(f"Added: {key} = {value}")
    
    else:
        # Default dictionary
        print("\nUsing default dictionary...")
        my_dict = {
            'name': 'John',
            'age': 30,
            'city': 'New York',
            'salary': 50000.50,
            'is_active': True,
            'skills': ['Python', 'Java', 'SQL']
        }
    
    # Display dictionary
    print("\n" + "="*50)
    print("DICTIONARY INFORMATION")
    print("="*50)
    print(f"\nComplete dictionary: {my_dict}")
    print(f"\nTotal number of key-value pairs: {len(my_dict)}")
    
    # Print all keys
    print_dict_keys(my_dict)
    
    # Print all values
    print_dict_values(my_dict)
    
    # Print all items
    print_dict_items(my_dict)
    
    # Additional information
    print(f"\n" + "="*50)
    print("ADDITIONAL INFORMATION")
    print("="*50)
    print(f"Dictionary type: {type(my_dict)}")
    print(f"Is dictionary empty? {len(my_dict) == 0}")


if __name__ == "__main__":
    main()

