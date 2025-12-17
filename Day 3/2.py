"""
Write a program to remove duplicates from a list.
"""


def remove_duplicates_preserve_order(lst):
    """Remove duplicates while preserving the order of first occurrence."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def remove_duplicates_set(lst):
    """Remove duplicates using set (does not preserve order)."""
    return list(set(lst))


def remove_duplicates_dict(lst):
    """Remove duplicates using dict.fromkeys (preserves order in Python 3.7+)."""
    return list(dict.fromkeys(lst))


def main():
    """Main function to remove duplicates from a list."""
    print("="*50)
    print("REMOVE DUPLICATES FROM LIST")
    print("="*50)
    print("\nEnter list elements (space-separated):")
    user_input = input().strip()
    
    if not user_input:
        print("No input provided. Using default list: [1, 2, 2, 3, 4, 4, 5, 1, 6]")
        my_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
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
    print(f"Original length: {len(my_list)}")
    
    # Method 1: Preserve order
    result1 = remove_duplicates_preserve_order(my_list)
    print(f"\nMethod 1 (Preserve Order): {result1}")
    print(f"Length after removing duplicates: {len(result1)}")
    
    # Method 2: Using dict.fromkeys (also preserves order)
    result2 = remove_duplicates_dict(my_list)
    print(f"\nMethod 2 (Using dict.fromkeys): {result2}")
    print(f"Length after removing duplicates: {len(result2)}")
    
    # Method 3: Using set (does not preserve order)
    result3 = remove_duplicates_set(my_list)
    print(f"\nMethod 3 (Using set - no order): {result3}")
    print(f"Length after removing duplicates: {len(result3)}")
    
    # Show removed elements
    removed = [x for x in my_list if my_list.count(x) > 1]
    removed_unique = list(dict.fromkeys(removed))
    if removed_unique:
        print(f"\nDuplicate elements that were removed: {removed_unique}")
    else:
        print("\nNo duplicates found in the list!")


if __name__ == "__main__":
    main()

