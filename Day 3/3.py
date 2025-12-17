"""
Write a program to find the sum and average of a list of numbers.
"""


def calculate_sum(lst):
    """Calculate the sum of all elements in the list."""
    return sum(lst)


def calculate_average(lst):
    """Calculate the average of all elements in the list."""
    if len(lst) == 0:
        return None
    return sum(lst) / len(lst)


def main():
    """Main function to calculate sum and average."""
    print("="*50)
    print("SUM AND AVERAGE CALCULATOR")
    print("="*50)
    print("\nEnter numbers (space-separated):")
    user_input = input().strip()
    
    if not user_input:
        print("No input provided. Using default list: [10, 20, 30, 40, 50]")
        numbers = [10, 20, 30, 40, 50]
    else:
        try:
            numbers = [float(x) for x in user_input.split()]
            # Convert to int if all are integers
            if all(x.is_integer() for x in numbers):
                numbers = [int(x) for x in numbers]
        except ValueError:
            print("Error: Please enter valid numbers only!")
            return
    
    if len(numbers) == 0:
        print("Error: List is empty! Cannot calculate sum or average.")
        return
    
    # Calculate sum and average
    total_sum = calculate_sum(numbers)
    average = calculate_average(numbers)
    
    # Display results
    print(f"\nList: {numbers}")
    print(f"Number of elements: {len(numbers)}")
    print(f"Sum: {total_sum}")
    
    if average is not None:
        # Format average to 2 decimal places if it's a float
        if isinstance(average, float) and not average.is_integer():
            print(f"Average: {average:.2f}")
        else:
            print(f"Average: {average}")
    else:
        print("Average: Cannot calculate (empty list)")
    
    # Additional statistics
    print(f"\nMinimum value: {min(numbers)}")
    print(f"Maximum value: {max(numbers)}")


if __name__ == "__main__":
    main()

