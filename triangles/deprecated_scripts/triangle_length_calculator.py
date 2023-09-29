#! /bin/python3

import math

def calculate_length(c, A):

    A_radians = math.radians(A)

    a = c * math.cos(A_radians)
    b = math.sqrt(c**2 - a**2)

    print(f" a: {a:.2f} units")
    print(f" b: {b:.2f} units")

def main():
    c = float(input(" Enter the value of c: "))
    A = float(input(" Enter the value of A: "))
    
    calculate_length(c, A)

if __name__ == "__main__":
    main()
