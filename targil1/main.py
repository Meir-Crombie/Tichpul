# Meir Crombie - 214736688
# Yedidia Bakuradze - 332461854
#  ================== QUESTION ONE ==================
def is_valid_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a
def check_triangle():
    a, b, c = map(float, input("Enter three numbers: ").split())
    if is_valid_triangle(a, b, c):
        print("correct triangle sides lengths")
    else:
        print("not correct triangle sides lengths")
#  ==================================================

#  ================== QUESTION TWO ==================
#appears in a separate file
#call it through the sort in this file and then there is a sort name for exercise 2
# ====================================================
# תרגיל 3 - הדפסת המספרים האמצעיים
# פונקציה למציאת שני המספרים האמצעיים (עם מיון)
def middle_two_sorted(nums):
    nums.sort()
    return nums[len(nums) // 2 - 1: len(nums) // 2 + 1]


# פונקציה למציאת שני המספרים האמצעיים (ללא מיון)
def middle_two_manual(nums):
    mid_nums = nums[:]  # יוצרים עותק של הרשימה כדי לא לפגוע בנתוני הקלט
    for _ in range(len(nums) // 2 - 1):  # מסירים את המספרים הכי קטנים והכי גדולים עד שנותרים שניים
        mid_nums.remove(min(mid_nums))
        mid_nums.remove(max(mid_nums))
    return mid_nums


# פונקציה לקבלת קלט והדפסת מספרים אמצעיים
def get_middle_numbers():
    nums = list(map(float, input("Enter four distinct numbers: ").split()))
    print("Sorted method:", middle_two_sorted(nums))
    print("Manual method:", middle_two_manual(nums))


# פונקציה למציאת המספרים האמצעיים עבור רשימה באורך זוגי
def get_middle_numbers_list():
    nums = list(map(float, input("Enter an even-length list of numbers: ").split()))
    print("Sorted method:", middle_two_sorted(nums))
    print("Manual method:", middle_two_manual(nums))


# פונקציה למציאת מספרים בלבד מרשומה מעורבת והדפסת המספרים האמצעיים
def get_middle_from_mixed_list():
    user_input = input("Enter a mixed list (separate values by spaces): ")
    items = user_input.split()  # מפצלים את הקלט לפי רווחים

    # מנסים להמיר למספרים - מתעלמים ממילים או תווים שאינם מספריים
    nums = []
    for item in items:
        try:
            nums.append(float(item))  # ניסיון להמיר למספר
        except ValueError:
            continue  # אם לא מספר, מתעלמים

    print("Filtered numbers:", nums)

    if len(nums) < 2:
        print("Not enough numeric values.")
        return

    if len(nums) % 2 == 0:
        print("Middle numbers:", middle_two_sorted(nums))
    else:
        print("List must have an even number of numeric values.")


# פונקציות שקשורות לפעולות על מספרים בינאריים- תרגיל 4
def shiftL(binNr, N):
    return binNr[N:] + '0' * N


def shiftR(binNr, N):
    return '0' * N + binNr[:-N]


def shiftCL(binNr, N):
    return binNr[N:] + binNr[:N]


def shiftCR(binNr, N):
    return binNr[-N:] + binNr[:-N]


# פונקציה לתפריט פעולות הזזה של מספרים בינאריים
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

            if choice == 1:  # Shift binary number left
                print(shiftL(binNr, N))
            elif choice == 2:  # Shift binary number right
                print(shiftR(binNr, N))
            elif choice == 3:  # Cyclic shift left
                print(shiftCL(binNr, N))
            elif choice == 4:  # Cyclic shift right
                print(shiftCR(binNr, N))
        else:
            print("Invalid choice")

# תרגיל 5 - ספירת סוגי נתונים ברשימה
def count_types(lst):
    type_counts = {}
    for item in lst:
        t = type(item).__name__
        type_counts[t] = type_counts.get(t, 0) + 1
    return type_counts

def list_types():
    print('Pls')
    lst = [1, 2, 'a', (11, 2, 'b'), [22, 'c'], (33,), ['d'], 'e']
    print(count_types(lst))


# תרגיל 6 - משחק ניחושים
def guess_game():
    import random
    N = random.randint(3, 9)
    target = tuple(random.sample(range(1, 10), N))
    while True:
        guess = tuple(map(int, input("Enter your guess (-1 to quit): ").split()))
        if guess == (-1,):
            break
        result = [guess[i] if guess[i] == target[i] else 'X' for i in range(N)]
        print("Result:", result)
        if result == list(target):
            print("Perfect guess!")
            break


# פונקציה ראשית להפעלת כל התרגילים
def main():
    options = [check_triangle, get_middle_numbers, get_middle_numbers_list, get_middle_from_mixed_list,
               shift_operations_menu, list_types, guess_game]
    descriptions = [
        "Check if three numbers can be triangle sides",
        "Find middle two numbers from four distinct numbers",
        "Find middle two numbers from an even-length list",
        "Extract numbers from a mixed list and find middle two",
        "Shift binary numbers operations",
        "Count data types in a list",
        "Guessing game"
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


# אם אתה רוצה להפעיל את זה במצב הרגיל:
if __name__ == "__main__":
    main()
