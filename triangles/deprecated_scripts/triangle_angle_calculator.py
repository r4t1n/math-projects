#! /bin/python3

import math

def calculate_angles(a, b, c):

    if a**2 + b**2 == c**2: # Ensure it is a right-angled triangle using Pythagorean thereom
        A = math.degrees(math.atan(b / a))
        B = 90 - A
        C = 90

        print(f" A: {A:.2f} degrees")
        print(f" B: {B:.2f} degrees")
        print(f" C: {C:.2f} degrees")
    else:
        print(" The given side lengths do not form a right-angled triangle")

def main():
    a = float(input(" Enter the value of a: "))
    b = float(input(" Enter the value of b: "))
    c = float(input(" Enter the value of c: "))
    
    calculate_angles(a, b, c)

if __name__ == "__main__":
    main()
