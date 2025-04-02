# Functional Programming
# Exercise 1 – Python

1. Three numbers can be the lengths of the sides of a triangle if they satisfy the triangle inequality, that is: a + b > c, a + c > b, c + b > a
   a. Write a Boolean function that takes three numbers (integers and/or real numbers) and checks whether they can be the lengths of a valid triangle.
   b. Write a Python program that receives three numbers from the keyboard and, using the function you wrote, checks whether they can be the lengths of the sides of a triangle.
   If yes, the program will print "correct triangle sides lengths"
   If no, the program will print "not correct triangle sides lengths".
   For example, for the input: a = 4, b = 3, c = 2.5 the output will be "correct triangle sides lengths"
   And for the input a = 20, b = 3.75, c = 2 the output will be "not correct triangle sides lengths"

2. In the file MenuForTar1.py provided in the model, there is a program that allows calculating areas of rectangles and circles according to the user's choice. You need to expand the program and add options to calculate areas of additional shapes such as triangle and square, as well as volumes of three-dimensional bodies such as sphere, cone, and square pyramid.
   (You can use Google for the formulas for these calculations)
   To do this:
   a. Write a function to calculate the area or perimeter of each of the shapes/bodies.
   b. Add additional selection options to the main menu
   c. Update the code to fit all the shapes and bodies you have defined.

3. a. Write a Python program that takes 4 different numbers from the user (integers or real numbers) and prints the 2 middle numbers (numbers that are greater than the minimum and smaller than the maximum). Write 2 versions of this function, one that uses the sort or sorted function and another without using any additional function.
   For example, for the input 100, 20, 35, 40, the program will print 35, 40.
   
   b. Write a generalization to section a and write a program that this time receives a tuple of any length (even length) of numbers (integers and/or real numbers), and prints the 2 middle numbers in size.
   For example, for the input (100, 20, 35, 40, 67, 32) the program will print 35, 40.
   Write two versions of this program: one that uses the sort() or sorted() method, and the other without using the above method (or function).
   
   c. Write another generalization of the above program, so that this time the program will receive a tuple of any length (even length) containing any values (that is, the tuple can be values of different types and even nested) and create a new tuple that contains only the numeric elements of the input tuple.
   The program will then run the function from section b on it and print the 2 middle numerical values in size.
   For example, for the input: (100, [20, 35, 'abc'], 40, "my test", 67, 32, 15, 34) the program will print 34, 35.

4. Binary numbers can be represented as strings of digits "0" and "1".
   You need to write four functions named shiftL, shiftR, shiftCL, shiftCR that accept two parameters: a binary number binNr (string) and a positive integer N that determines how many places to move.
   
   shiftL "moves" the binary number N places "to the left". As a result of the move, the N leftmost binary digits "fall off", and N "0" digits are inserted at the beginning of the new binary number.
   >>> shiftL("110001110", 2)
   "000111000"
   
   shiftR "moves" the binary number N places "to the right". As a result of the move, the N rightmost binary digits "fall off", and N "0" digits are inserted at the end of the new binary number.
   >>> shiftR("110001110", 2)
   "001100011"
   
   shiftCL "moves" the binary number N places "to the left". As a result of the move, the N leftmost binary digits, which in shiftL would "fall off", are inserted at the beginning of the new binary number.
   >>> shiftCL("110001110", 2)
   "000111011"
   
   shiftCR "moves" the binary number N places "to the right". As a result of the move, the N rightmost binary digits, which in shiftR would "fall off", are inserted at the end of the new binary number.
   >>> shiftCR("1100011", 2)
   "1111000"
   
   Hint: Use appropriate slices to implement all four functions above. Note that no loops are needed.

5. Write a Python program that receives a list containing integers, strings, tuples, and lists. Write appropriate functions that will allow the program to count the total number of tuples, lists, numbers, and strings found in the input list. The program will print the results that the above functions return.
   Use a dictionary to count the different types of data in the input list, so that the name of the data type will be a key, and the counter will be the value associated with that key.
   For example, if we use the list
   L = [1, 2, 'a', (11, 2, 'b'), [22, 'c'], (33,), ['d'], 'e'],
   the dictionary that will be created is
   D = {list: 2, int: 2, float: 0, str: 2, tuple: 2}
   The required output for this input example (and the dictionary created for it) is:
   Total tuples: 2, Total lists: 2, Total numbers: 2, Total strings: 2
   Implement all the above functions using appropriate for loops.
   
   The Python file (actually, the module) in which you wrote the above program must be written so that it can be run as a full program, and also that it can be imported as a module from any other module (or program), without the import running the executable part of the program (actually the main of the program).

6. Write a Python program that creates a tuple with 3<=N<=9 integers that are randomly selected from the range 1-9 (including endpoints - duplicates are allowed), and does not print it (although it's good to print it temporarily when writing the program for testing purposes and remove the print before submission).
   The program will do the following:
   a. Ask the user to enter N integers between 1 and 9 (inclusive, duplicates allowed) as a guess for the N numbers that were randomly selected.
   b. Store the N guess numbers in a tuple. Note that the position of the numbers has meaning.
   c. Call a function named nihushTest that receives as its first parameter the tuple of randomly selected numbers, and an unknown number of integers that are supposed to be the N guess numbers. The function will check the correctness of the guess number, in value and position, relative to the tuple of N randomly selected numbers. The function will return a tuple in which all numbers that were correct guesses will appear in their positions, and the string "X" will appear in all places where the guess was incorrect.
   d. The program will print on the same line, the tuple that the nihushTest function returned, and the percentage of successful guessing.
   The user will play several times, according to his wish. The guessing game will stop when the user enters the number -1, or when the guess he entered was perfect (all guess numbers were correct). At the end, the program will print the tuple of numbers that were randomly selected by the computer at the beginning of the game.
   In addition, the program will calculate and print maxpct, the highest success percentage of guessing obtained in the different rounds of the game.
