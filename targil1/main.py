# Meir Crombie - 214736688
# Yedidia Bakuradze - 332461854
from MenuForTar1 import menu_shapes

#  ================== QUESTION ONE ==================
# Function to check if given sides can form a valid triangle
def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Function to input triangle sides and check their validity
def check_triangle():
    a, b, c = map(float, input("Enter three numbers: ").split())
    if is_valid_triangle(a, b, c):
        print("Correct triangle sides lengths")
    else:
        print("Not correct triangle sides lengths")
#  ==================================================

#  ================== QUESTION TWO ==================
# In the main there is call for the menu from the other file
#  ================== QUESTION THREE ==================
# Function to find two middle numbers using sorted method
def middle_two_sorted(nums):
    nums.sort()
    return nums[len(nums) // 2 - 1: len(nums) // 2 + 1]

# Function to find two middle numbers manually without sorting
def middle_two_manual(nums):
    mid_nums = nums[:]
    for _ in range(len(nums) // 2 - 1):
        mid_nums.remove(min(mid_nums))
        mid_nums.remove(max(mid_nums))
    return mid_nums

# Function to get four distinct numbers and print their middle numbers
def get_middle_numbers():
    nums = list(map(float, input("Enter four distinct numbers: ").split()))
    print("Sorted method:", middle_two_sorted(nums))
    print("Manual method:", middle_two_manual(nums))

# Function to get middle numbers from an even-length list
def get_middle_numbers_list():
    nums = list(map(float, input("Enter an even-length list of numbers: ").split()))
    print("Sorted method:", middle_two_sorted(nums))
    print("Manual method:", middle_two_manual(nums))

# Function to extract and find middle numbers from a mixed list
def get_middle_from_mixed_list():
    user_input = input("Enter a mixed list (separate values by spaces): ")
    items = user_input.split()

    nums = []
    for item in items:
        try:
            nums.append(float(item))
        except ValueError:
            continue

    print("Filtered numbers:", nums)

    if len(nums) < 2:
        print("Not enough numeric values.")
        return

    if len(nums) % 2 == 0:
        print("Middle numbers:", middle_two_sorted(nums))
    else:
        print("List must have an even number of numeric values.")
# ====================================================
#  ================== QUESTION FOUR ==================

# Functions for binary number shift operations
def shiftL(binNr, N):
    return binNr[N:] + '0' * N

def shiftR(binNr, N):
    return '0' * N + binNr[:-N]

def shiftCL(binNr, N):
    return binNr[N:] + binNr[:N]

def shiftCR(binNr, N):
    return binNr[-N:] + binNr[:-N]

# Menu for binary number shift operations
def shift_operations_menu():
    while True:
        print("Choose a shift operation:")
        print("1. Shift binary number left")
        print("2. Shift binary number right")
        print("3. Cyclic shift left")
        print("4. Cyclic shift right")
        print("0. Exit to main menu")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if choice == 0:
            break
        elif 1 <= choice <= 4:
            binNr = input("Enter binary number: ")
            N = int(input("Enter the number of positions to shift: "))

            if choice == 1:
                print(shiftL(binNr, N))
            elif choice == 2:
                print(shiftR(binNr, N))
            elif choice == 3:
                print(shiftCL(binNr, N))
            elif choice == 4:
                print(shiftCR(binNr, N))
        else:
            print("Invalid choice")
# ====================================================

#  ================== QUESTION FIVE ==================
# Function to count types of elements in a list
def count_types(lst):
    type_counts = {}
    for item in lst:
        t = type(item).__name__
        type_counts[t] = type_counts.get(t, 0) + 1
    return type_counts

# Function to demonstrate type counting
def list_types():
    # Input: List containing integers, strings, tuples, and lists
    try:
        user_input = eval(input("Enter an array of values: \n>>> "))
    except SyntaxError:
        print("Provide non empty input")
        return

    # Count the types in the list
    print(count_types(user_input))
# ====================================================

#  ================== QUESTION SIX ==================
# Function to test guessing game
def nihushTest(target, guess):
    if len(target) != len(guess):
        raise ValueError("Guess length must match original numbers")

    result = []
    for i in range(len(target)):
        if guess[i] == target[i]:
            result.append(guess[i])
        else:
            result.append('X')

    return tuple(result)

# Main game logic for guessing game
def guess_game():
    import random
    maxpct = 0
    while True:
        N = random.randint(3, 9)
        target = tuple(random.sample(range(1, 10), N))
        print(f"Game selected with {N} numbers")
        user_input = input(f"Enter {N} numbers between 1-9 (or -1 to quit): ")
        if user_input == '-1':
            break
        try:
            guess = tuple(map(int, user_input.split()))
            if len(guess) != N or any(num < 1 or num > 9 for num in guess):
                print(f"Please enter exactly {N} numbers between 1-9")
                continue
            result = nihushTest(target, guess)
            success_count = sum(1 for x in result if x != 'X')
            success_pct = (success_count / N) * 100
            maxpct = max(maxpct, success_pct)
            print(f"Guess result: {result}")
            print(f"Success percentage: {success_pct:.1f}%")
            if list(result) == list(target):
                print("Congratulations! You guessed all numbers correctly!")
                break
        except ValueError as e:
            print(f"Error: {e}")
    print(f"\nRandom numbers selected at the start: {target}")
    print(f"Maximum success percentage in the game: {maxpct:.1f}%")
# ====================================================
#  ================== QUESTION MAIN ==================
# Main function to run all exercises
def main():
    options = [check_triangle,menu_shapes, get_middle_numbers, get_middle_numbers_list, get_middle_from_mixed_list,
               shift_operations_menu, list_types, guess_game]
    descriptions = [
        "Targil 1 - Check if three numbers can be triangle sides",
        "Targil 2 - menu for all shapes",
        "Targil 3.1 - Find middle two numbers from four distinct numbers",
        "Targil 3.2 - Find middle two numbers from an even-length list",
        "Targil 3.3 - Extract numbers from a mixed list and find middle two",
        "Targil 4 - Shift binary numbers operations",
        "Targil 5 - Count data types in a list",
        "Targil 6 - Guessing game"
    ]
    while True:
        print("Choose an option:")
        for i, desc in enumerate(descriptions, 1):
            print(f"{i}. {desc}")
        print("0. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        if choice == 0:
            break
        elif 1 <= choice <= len(options):
            options[choice - 1]()
        else:
            print("Invalid choice")

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()