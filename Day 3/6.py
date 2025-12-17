"""
Write a program to count the frequency of each element in a list using a dictionary.
"""


def count_frequency(lst):
    """Count the frequency of each element in the list using a dictionary."""
    frequency = {}
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    return frequency


def count_frequency_counter(lst):
    """Count frequency using collections.Counter (alternative method)."""
    from collections import Counter
    return dict(Counter(lst))


def display_frequency(frequency_dict):
    """Display the frequency dictionary in a formatted way."""
    print("\n" + "="*50)
    print("FREQUENCY COUNT")
    print("="*50)
    print(f"{'Element':<15} {'Frequency':<10}")
    print("-" * 25)
    
    # Sort by frequency (descending), then by element (ascending)
    sorted_items = sorted(frequency_dict.items(), key=lambda x: (-x[1], str(x[0])))
    
    for element, count in sorted_items:
        print(f"{str(element):<15} {count:<10}")
    
    print("="*50)


def main():
    """Main function to count element frequencies."""
    print("="*50)
    print("COUNT FREQUENCY OF ELEMENTS IN LIST")
    print("="*50)
    print("\nEnter list elements (space-separated):")
    user_input = input().strip()
    
    if not user_input:
        print("No input provided. Using default list: [1, 2, 3, 2, 1, 4, 2, 5, 1, 3]")
        my_list = [1, 2, 3, 2, 1, 4, 2, 5, 1, 3]
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
    
    # Count frequency
    frequency = count_frequency(my_list)
    
    # Display results
    print(f"\nFrequency dictionary: {frequency}")
    display_frequency(frequency)
    
    # Additional statistics
    print(f"\nTotal unique elements: {len(frequency)}")
    print(f"Most common element(s): {[k for k, v in frequency.items() if v == max(frequency.values())]}")
    print(f"Highest frequency: {max(frequency.values())}")
    print(f"Least common element(s): {[k for k, v in frequency.items() if v == min(frequency.values())]}")
    print(f"Lowest frequency: {min(frequency.values())}")


if __name__ == "__main__":
    main()

