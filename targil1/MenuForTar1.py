#
#  Example program for Targil 1
import math


# פונקציות לחישוב שטחים ונפחים
def rectangle_area(w, h):
    return w * h

def square_area(s):
    return s * s

def circle_area(r):
    return math.pi * r ** 2

def triangle_area(b, h):
    return 0.5 * b * h

def sphere_volume(r):
    return (4/3) * math.pi * r ** 3

def cone_volume(r, h):
    return (1/3) * math.pi * r ** 2 * h

def pyramid_volume(b, h):
    return (1/3) * b ** 2 * h
#הדפסת תפריט הצורות
def prtMenu(shapes):
    for i in range(len(shapes)):
        print(i + 1, shapes[i])

# תוכנית ראשית לחישוב שטחים ונפחים
def menu_shapes():
    shapes = ("Rectangle", "Square", "Circle", "Triangle", "Sphere", "Cone", "Pyramid")
    while True:
        print("\nPlease select a shape (press 0 to quit):")
        prtMenu(shapes)
        shape = input("> ")
        if shape == "1":
            height = float(input("Please enter the height: "))
            width = float(input("Please enter the width: "))
            print("The area is", rectangle_area(width, height))
        elif shape == "2":
            side = float(input("Please enter the side length: "))
            print("The area is", square_area(side))
        elif shape == "3":
            radius = float(input("Please enter the radius: "))
            print("The area is", circle_area(radius))
        elif shape == "4":
            base = float(input("Please enter the base length: "))
            height = float(input("Please enter the height: "))
            print("The area is", triangle_area(base, height))
        elif shape == "5":
            radius = float(input("Please enter the radius: "))
            print("The volume is", sphere_volume(radius))
        elif shape == "6":
            radius = float(input("Please enter the radius: "))
            height = float(input("Please enter the height: "))
            print("The volume is", cone_volume(radius, height))
        elif shape == "7":
            base = float(input("Please enter the base length: "))
            height = float(input("Please enter the height: "))
            print("The volume is", pyramid_volume(base, height))
        elif shape == "0":
            print("Bye!")
            break
        else:
            print("Invalid shape")
