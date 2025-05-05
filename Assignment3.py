"""
שיפור קוד מחדש כך שיהיה תואם לקוד המקורי של Dvir Diei ו-Oriya Hanuka
הקוד משמר את האלגוריתמים המקוריים בכל חמש השאלות
"""

# Function to generate pentagonal numbers in a range using recursion
def pentaNumRagnge1(n1, n2):
    # Lambda function to calculate the pentagonal number for a given index
    getPentaNum = lambda x: x / 2 * (3 * x - 1)

    # Helper function to recursively build the list of pentagonal numbers
    def help(acc, n1, n2):
        # Base case: if n1 >= n2, return the accumulated list
        if n1 >= n2:
            return acc
        # Recursive case: add the current pentagonal number to the list and increment n1
        return help(acc + [getPentaNum(n1)], n1 + 1, n2)

    return help([], n1, n2)

# Function to generate pentagonal numbers in a range using recursion (reverse order)
def pentaNumRagnge2(n1, n2):
    # Lambda function to calculate the pentagonal number for a given index
    getPentaNum = lambda x: x / 2 * (3 * x - 1)

    # Helper function to recursively build the list of pentagonal numbers
    def help2(n1, n2):
        # Base case: if n1 >= n2, return an empty list
        if n1 >= n2:
            return []
        # Recursive case: calculate the pentagonal number and append it after the recursive call
        return help2(n1 + 1, n2) + [getPentaNum(n1)]

    return help2(n1, n2)

# Function to handle user input and print pentagonal numbers
def f1():
    try:
        n1 = int(input("Enter the value of n1: "))
        n2 = int(input("Enter the value of n2: "))
        # Validate input: n1 and n2 must be positive integers, and n2 > n1
        if n1 <= 0 or n2 <= 0 or n1 >= n2:
            return print("ERROR: The values must be positive integers and n2 > n1.")

        # Generate pentagonal numbers using both methods
        num_list = pentaNumRagnge1(n1, n2)
        num_list2 = pentaNumRagnge2(n1, n2)

        # Print the results in rows of 10 numbers
        for i in range(len(num_list)):
            print(f"{num_list[i]}", end=" ")
            if (i + 1) % 10 == 0:
                print()

        print()
        for i in range(len(num_list2)):
            print(f"{num_list2[i]}", end=" ")
            if (i + 1) % 10 == 0:
                print()

    except ValueError:
        # Handle invalid input
        print("ERROR: The values must be positive integers and n2 > n1.")

# Function to reverse an integer using recursion
def reverseNum1(n):
    # Lambda functions for mathematical operations
    getRemainder = lambda x, y: x % y
    multiplyBy10 = lambda x: x * 10

    # Helper function to recursively reverse the number
    def helpre(n, m, x):
        # Base case: if the length of the reversed number matches the original, return the result
        if len(str(n)) == len(str(m)):
            return m
        else:
            # Recursive case: extract the last digit and append it to the reversed number
            return helpre(n, int(getRemainder(n, x * 10) / x) + multiplyBy10(m), multiplyBy10(x))

    # Handle negative numbers
    if n < 0:
        return -helpre(-n, 0, 1)
    return helpre(n, 0, 1)

# Function to reverse an integer using recursion (alternative method)
def reverseNum2(n):
    # Lambda functions for mathematical operations
    getRemainderBy10 = lambda x: int(x / 10)
    getRemainder = lambda x, y: x % y

    # Helper function to recursively reverse the number
    def helpre2(n, x):
        # Base case: if the number has only one digit, return it
        if len(str(n)) == 1:
            return n
        # Recursive case: extract the last digit and append it to the reversed number
        return helpre2(getRemainderBy10(n), getRemainderBy10(x)) + getRemainder(n, 10) * x

    # Handle negative numbers
    if n < 0:
        return -helpre2(-n, int(10 ** len(str(n)) / 100))
    return helpre2(n, int(10 ** len(str(n)) / 10))

# Function to handle user input and reverse a number
def f2():
    try:
        number = int(input("Enter an integer number n (positive or negative): "))
        # Print the reversed number using both methods
        print(f"Reversed number: {reverseNum1(number)}")
        print(f"Reversed number: {reverseNum2(number)}")
    except ValueError:
        # Handle invalid input
        print("ERROR: Input number is incorrect!")

# Function to compute Pi using recursive methods
def f3():
    try:
        n = int(input("Enter a Natural number n: "))
        # Validate input: n must be a positive integer
        if n < 1:
            print("ERROR: Input number is incorrect!")
        else:
            # Compute and print Pi using both recursive methods
            list(map(lambda i: print(i, pi_recursive(i)), range(1, n + 1)))
            list(map(lambda i: print(i, pi_tail_recursive(i)), range(1, n + 1)))
    except ValueError:
        print("ERROR: Input number is incorrect!")

# Recursive function to compute Pi
def pi_recursive(n):
    # Lambda function to calculate the term in the series
    getTerm = lambda i: 4 * ((-1) ** (i + 1) / (2 * i - 1))

    # Helper function to recursively compute the sum
    def rec(i):
        # Base case: return the first term
        if i == 1:
            return getTerm(1)
        # Recursive case: add the current term to the sum of previous terms
        return getTerm(i) + rec(i - 1)

    return rec(n)

# Tail-recursive function to compute Pi
def pi_tail_recursive(n):
    # Lambda function to calculate the term in the series
    getTerm = lambda i: ((-1) ** (i + 1)) / (2 * i - 1)

    # Helper function to recursively compute the sum
    def help(n, acc):
        # Base case: if n == 0, return the accumulated sum multiplied by 4
        if n == 0:
            return 4 * acc
        # Recursive case: add the current term to the accumulator
        return help(n - 1, acc + getTerm(n))

    return help(n, 0.0)

# Function to find twin primes
def f4():
    try:
        n = int(input("Enter a Natural number n: "))
        # Validate input: n must be a positive integer
        if n < 1:
            print("ERROR: Input number is incorrect!")
        else:
            # Find twin primes using both methods
            primes = twinp(n)
            twin_pairs = list(filter(lambda pair: pair[1] - pair[0] == 2, zip(primes, primes[1:])))
            list(map(lambda pair: print(pair[0], pair[1]), twin_pairs))
            primes2 = twinp_tail(n)
            twin_pairs2 = list(filter(lambda pair: pair[1] - pair[0] == 2, zip(primes2, primes2[1:])))
            list(map(lambda pair: print(pair[0], pair[1]), twin_pairs2))
    except ValueError:
        print("ERROR: Input number is incorrect!")

# Recursive function to find prime numbers
def twinp(n):
    # Helper function to implement the sieve of Eratosthenes
    def sieve(numbers):
        # Base case: if the list is empty, return an empty list
        if not numbers:
            return []
        head = numbers[0]
        # Recursive case: filter out multiples of the current prime and continue
        recursive_filter = lambda p: [] if not p else (
            recursive_filter(p[1:]) if p[0] % head == 0 else [p[0]] + recursive_filter(p[1:])
        )
        return [head] + sieve(recursive_filter(numbers[1:]))

    return sieve(list(range(2, n)))

# Tail-recursive function to find prime numbers
def twinp_tail(n):
    # Helper function to implement the sieve of Eratosthenes
    def sieve(remaining, acc):
        # Base case: if the list is empty, return the accumulated primes
        if not remaining:
            return acc
        head = remaining[0]
        # Recursive case: filter out multiples of the current prime and continue
        recursive_filter = lambda p: [] if not p else (
            recursive_filter(p[1:]) if p[0] % head == 0 else [p[0]] + recursive_filter(p[1:])
        )
        return sieve(recursive_filter(remaining[1:]), acc + [head])

    return sieve(list(range(2, n)), [])

# Function to merge three dictionaries
def add3dicts(d1, d2, d3):
    # Helper lambdas for set operations
    combine = lambda a, b, c: a & b & c
    difference = lambda a, b, c: (a - b - c) | (b - a - c) | (c - a - b)
    difference2 = lambda a, b, c: ((a & b) - c) | ((a & c) - b) | ((b & c) - a)

    # Helper lambdas for merging dictionaries
    mergeDicts = lambda d1, d2: {**d1, **d2}
    mergeKey2 = lambda key, D1, D2: {key: (D1[key], D2[key])}
    mergeKey3 = lambda key, D1, D2, D3: {key: (D1[key], D2[key], D3[key])}

    # Recursive helper function to build the merged dictionary
    def help_add(d1, d2, d3, set, d4, mode="combine3"):
        # Base case: if the set is empty, return the accumulated dictionary
        if len(set) == 0:
            return d4

        workOn = next(iter(set))

        # Handle different modes for merging
        if mode == "combine3":
            tempDic = mergeKey3(workOn, d1, d2, d3)
        elif mode == "combine2":
            if workOn in d1:
                tempDic = {workOn: d1[workOn]}
            elif workOn in d2:
                tempDic = {workOn: d2[workOn]}
            elif workOn in d3:
                tempDic = {workOn: d3[workOn]}
        elif mode == "withoutCommon":
            if workOn in d1 and workOn in d2:
                tempDic = mergeKey2(workOn, d1, d2)
            elif workOn in d1 and workOn in d3:
                tempDic = mergeKey2(workOn, d1, d3)
            else:
                tempDic = mergeKey2(workOn, d2, d3)

        return help_add(d1, d2, d3, set - {workOn}, mergeDicts(d4, tempDic), mode)

    # Combine dictionaries based on different criteria
    dicCombine = help_add(d1, d2, d3, combine(set(d1), set(d2), set(d3)), {})
    dicDifference = help_add(d1, d2, d3, difference(set(d1), set(d2), set(d3)), {}, "combine2")
    dicDifference2 = help_add(d1, d2, d3, difference2(set(d1), set(d2), set(d3)), {}, "withoutCommon")
    return mergeDicts(dicDifference2, mergeDicts(dicDifference, dicCombine))

# Function to handle user input and merge dictionaries
def f5():
    try:
        d1 = eval(input("Enter a dictionary: "))
        d2 = eval(input("Enter a dictionary: "))
        d3 = eval(input("Enter a dictionary: "))

        # Validate input: all inputs must be dictionaries
        if not all(isinstance(d, dict) for d in (d1, d2, d3)):
            raise ValueError("Input is not a dictionary")

        # Merge dictionaries using the function
        result = add3dicts(d1, d2, d3)
        print(result)

    except (SyntaxError, ValueError):
        # Handle invalid input
        print("ERROR: Input is incorrect!")

def main():
    while True:
        print("\nMain Menu:")
        print("1. f1 - Generate pentagonal numbers in a range")
        print("2. f2 - Reverse an integer number")
        print("3. f3 - Compute Pi using recursive methods")
        print("4. f4 - Find twin primes")
        print("5. f5 - Merge three dictionaries")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            f1()
        elif choice == "2":
            f2()
        elif choice == "3":
            f3()
        elif choice == "4":
            f4()
        elif choice == "5":
            f5()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()