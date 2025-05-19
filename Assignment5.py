# Yedidia Bakuradze: 332461854
# Meir Crombie: 214736688

from ast import literal_eval

def evenprt(n1: int, n2: int, n3: int) -> None:

    # Prints even numbers in a range, grouped by a given size.
    def even(n1: int, n2: int):

        # Generates even numbers within a range (from n1 to n2 ).
        if n1 > n2:
            return
        if n1 % 2 == 1:
            n1 += 1
        if n1 <= n2:  # Only yield if the number is within range
            yield n1
            yield from even(n1 + 2, n2)

    # Groups and prints elements from a generator that x (n3) elements on one line.
    def group(list_gen, size: int, now: int = 0) -> None:
        try:
            i = next(list_gen)
            print(i, end=" ")
            if (now + 1) % size == 0:
                print()
            group(list_gen, size, now + 1)
        except StopIteration:
            return

    group(even(n1,n2),n3)

def q1() -> None:
    try:
        n1=int(input("Enter the value of N1:"))
        n2=int(input("Enter the value of N2:"))
        n3=int(input("Enter the value of N3:"))
        if n1>n2 or n3 <= 0 or n3 > (n2-n1+1)//2 + ((n2-n1+1) % 2):
            return print("ERROR: at least one of the input values is incorrect")
        evenprt(n1,n2,n3)
    except ValueError:
        return print("ERROR: at least one of the input values is incorrect")

def q2() -> None:
    try:
        n = int(input("Enter a number: "))
        if n <= 0:
            return print("ERROR: the number must be a positive integer")
        print(primefactors(n))
    except ValueError:
        return print("ERROR: the number must be a positive integer")

def napa(n: int) -> list:

    def calc(nums: list) -> list:
        return [] if not nums else [nums[0]] + calc([p for p in nums[1:] if p % nums[0] != 0])

    return [1] + calc([x for x in range(2, n + 1)])  # + 1 is in case the number is a prime 

def primefactors(n: int) -> list:
    return [p for p in napa(n) if n % p == 0]


def sortkey():
    def key(x):
        return (isinstance(x, str), x)
    yield key


def sortedzip(lists):
    return (
        tuple(items)
        for items in zip(*(sorted(sub, key = next(sortkey())) for sub in lists))
    )


def reversedzip(lists):
    return (
        tuple(items)
        for items in zip(*(reversed(sub) for sub in lists))
    )


def funczip(func, lists):
    return func(lists)


def unzippy(zipped):
    return (
        list(group)
        for group in zip(*zipped)
    )


def q3():
    try:
        n = int(input("Enter the size of the sublists of the list to process: "))
        if n <= 0:
            print("ERROR - size must be a positive integer")
            return
            
        l = literal_eval(input("Enter the list to process: "))

        if not (isinstance(l, list) and all(isinstance(sub, list) for sub in l)):
            print("ERROR - input must be a list of lists.")
            return
        if not all(len(sub) == n for sub in l):
            print(f"ERROR - all sublists must be of size {n}")
            return

        dispatch = {'1': sortedzip, '2': reversedzip}

        print("1: sortedzip")
        print("2: reversedzip")
        choice = input("Which function do you want to choose? ")
        if choice not in dispatch:
            print("ERROR - chosen function does not exist.")
            return

        result = list(funczip(dispatch[choice], l))
        print(result)
        print(list(unzippy(result)))
    except ValueError:
        print("ERROR - invalid input")

def main():
    while True:
        print("\nFunctional Programming Exercise Menu")
        print("1: Print even numbers in range")
        print("2: Find prime factors of a number")
        print("3: List processing functions")
        print("0: Exit")
        
        try:
            choice = int(input("Enter your choice (0-3): "))
            
            if choice == 0:
                print("Exiting program. Goodbye!")
                break
            elif choice == 1:
                q1()
            elif choice == 2:
                q2()
            elif choice == 3:
                q3()
            else:
                print("Invalid choice. Please enter a number between 0 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()


