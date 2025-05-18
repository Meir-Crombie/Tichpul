import ast

# Yedidia Bakuradze: 332461854
# Meir Crombie: 214736688


# Function to read exam information from a file
def get_exam_info(file_name):
    flobj = open(file_name, "r")  # Open the file in read mode
    lines = flobj.readlines()  # Read all lines from the file
    flobj.close()  # Close the file
    return [line[:-1].split(",") for line in lines]  # Process each line and split by commas

# Function to calculate project times
def calcProjectTimes(file_name):
    less = lambda x, y: x - y  # Lambda function to calculate the difference

    if not file_name:  # If the file name is empty, return an empty list
        return []

    head, *tail = file_name  # Split the file name into head and tail

    # Helper function to process the file
    def calcProjectTimesTail(file_only):
        if not file_only[0]:  # If the first element is empty, return an empty list
            return []

        head, *tail = file_only  # Split the file into head and tail
        if isinstance(head[0], list):  # If the first element is a list, process recursively
            return [calcProjectTimes(head)]
        return [[head[0], less(head[2], head[1])]] + [calcProjectTimesTail(tail)]  # Calculate time differences

    return [calcProjectTimesTail(head)] + calcProjectTimes(tail)  # Combine results recursively

# Function to calculate project time and cost
def proj_time_cost(file_name, cost_per_time_unit):
    # Helper function to sum specific values from the file
    def proj_time_cost_tail(file, num_check):
        data = [sublist[0] for sublist in file]  # Extract the first element of each sublist
        return sum([sublist[num_check] for sublist in data])  # Sum the specified values

    x1 = proj_time_cost_tail(file_name, 1)  # Calculate total time
    x2 = proj_time_cost_tail(file_name, 2)  # Calculate total cost
    x3 = proj_time_cost_tail(calcProjectTimes(file_name), 1)  # Calculate adjusted time
    return ((x1, x1 * cost_per_time_unit),  # Return time and cost tuples
            (x2, x2 * cost_per_time_unit),
            (x3, x3 * cost_per_time_unit))

# Function to handle project time and cost calculations
def q1():
    file_name = input("Enter the name of file: ")  # Get file name from user
    print(f"{calcProjectTimes(file_name)}")  # Print project times
    print(f"{proj_time_cost(file_name)}")  # Print project time and cost

# Function to reverse a list
def reverseList(lst):
    if not lst:  # Base case: if the list is empty, return an empty list
        return []

    head = lst[0]  # Get the first element
    tail = lst[1:]  # Get the rest of the list

    if isinstance(head, list):  # If the head is a list, reverse it recursively
        head_reversed = reverseList(head)
    elif isinstance(head, tuple):  # If the head is a tuple, reverse it recursively
        head_reversed = tuple(reverseList(list(head)))
    elif isinstance(head, str):  # If the head is a string, reverse the string
        head_reversed = head[::-1]
    else:  # Otherwise, keep the head as is
        head_reversed = head

    return reverseList(tail) + [head_reversed]  # Combine reversed tail and head

# Function to handle reversing a list
def q2():
    list_str = input("Enter a list: ")  # Get list input from user
    input_list = ast.literal_eval(list_str)  # Safely evaluate the input as a Python object

    if not isinstance(input_list, list):  # Validate input
        print("Invalid input: Please enter a valid list.")
        return
    print(reverseList(input_list))  # Print the reversed list

# Function to check if a list is a palindrome
def isPalindrome(lst):
    if len(lst) < 1:
        return True
    head, tail = lst[0], lst[-1]  # Get the first and last elements
    if isinstance(head, (list, tuple)) and isinstance(tail, (list, tuple)):  # If both are lists/tuples
        return isPalindrome(list(head) + list(tail)) and isPalindrome(lst[1:-1])
    elif isinstance(head, str) and isinstance(tail, str):  # If both are strings
        return head == tail[::-1] and isPalindrome(lst[1:-1])
    elif head == tail:  # If both are equal
        return isPalindrome(lst[1:-1])
    return False  # Otherwise, it's not a palindrome

# Function to handle palindrome checking
def q3():
    list_str = input("Enter a list: ")  # Get list input from user
    input_list = ast.literal_eval(list_str)  # Safely evaluate the input as a Python object

    if not isinstance(input_list, list):  # Validate input
        print("Invalid input: Please enter a valid list.")
        return

    if isPalindrome(input_list):  # Check if the list is a palindrome
        print("It is a palindrome")
    else:
        print("It is not a palindrome")

# Function to find prime numbers using the sieve of Eratosthenes
def twinp(n):
    def twinpInner(numbers):
        if not numbers:  # Base case: if the list is empty, return an empty list
            return []

        head = numbers[0]  # Get the first number
        filtered = [x for x in numbers[1:] if x % head != 0] 
        return [head] + twinpInner(filtered)  # Combine the current prime with the rest

    return twinpInner(list(range(2, n)))  # Generate primes up to n

# Function to find and print twin primes
def q4():
    n = int(input("Enter a Natural number n: "))  # Get input from user
    if n < 1:  # Validate input
        print("ERROR: Input number is incorrect!")
    else:
        primes = twinp(n)  # Find primes up to n
        twin_pairs = [(a, b) for a, b in zip(primes, primes[1:]) if b - a == 2]  # Find twin primes
        [print(a, b) for a, b in twin_pairs]  # Print twin primes

# Function to merge three dictionaries
def add3dicts(dict1, dict2, dict3):
    keys1, keys2, keys3 = set(dict1), set(dict2), set(dict3)  # Get keys from all dictionaries

    keys12 = keys1 & keys2  # Common keys between dict1 and dict2
    keys13 = keys1 & keys3  # Common keys between dict1 and dict3
    keys23 = keys2 & keys3  # Common keys between dict2 and dict3
    combine_keys = keys12 & keys3  # Common keys among all three dictionaries

    # Combine items for keys common to all three dictionaries
    combine_items = [(key, (dict1[key], dict2[key], dict3[key])) for key in combine_keys]

    # Keys that are unique to one dictionary
    single_keys = ((keys1 - keys12 - keys13) | (keys2 - keys12 - keys23) | (keys3 - keys13 - keys23))

    # Items for keys unique to one dictionary
    single_items = [(key, dict1.get(key, dict2.get(key, dict3.get(key)))) for key in single_keys]

    # Keys that are common to exactly two dictionaries
    pairwise_keys = (keys12 | keys13 | keys23) - combine_keys
    pairwise_items = [
        (
            key,
            (dict1[key], dict2[key]) if key in keys12 else
            (dict1[key], dict3[key]) if key in keys13 else
            (dict2[key], dict3[key])
        )
        for key in pairwise_keys
    ]

    # Combine all items into a single dictionary
    return dict(single_items + pairwise_items + combine_items)

# Function to handle merging three dictionaries
def q5():
    try:
        d1 = eval(input("Enter a dictionary: "))  # Get first dictionary from user
        d2 = eval(input("Enter a dictionary: "))  # Get second dictionary from user
        d3 = eval(input("Enter a dictionary: "))  # Get third dictionary from user

        # Validate input: all inputs must be dictionaries
        if not all(isinstance(d, dict) for d in (d1, d2, d3)):
            raise ValueError("Input is not a dictionary")

        # Merge dictionaries using the function
        result = add3dicts(d1, d2, d3)
        print(result)  # Print the merged dictionary

    except (SyntaxError, ValueError):  # Handle invalid input
        print("ERROR: Input is incorrect!")

# Add a main menu to allow the user to choose a function
def main():
    while True:
        print("\nChoose a function to execute:")
        print("1. f1 - Handle project time and cost calculations")
        print("2. f2 - Reverse a list")
        print("3. f3 - Check if a list is a palindrome")
        print("4. f4 - Find and print twin primes")
        print("5. f5 - Merge three dictionaries")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            q1()
        elif choice == "2":
            q2()
        elif choice == "3":
            q3()
        elif choice == "4":
            q4()
        elif choice == "5":
            q5()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
