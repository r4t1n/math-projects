#! /bin/python3

import math

def calculate_type(a, b, c):
    epsilon = 1e-6 # Floating points suck so we give Python a little space to calculate :3

    sqrt_a_plus_b_power_two = math.sqrt(a**2 + b**2)
    print(" Square root of a^2 + b^2 =", sqrt_a_plus_b_power_two)

    if math.isclose(sqrt_a_plus_b_power_two, c, rel_tol=epsilon): # Essentially the same as "if sqrt_a_plus_b_power_two == c:" but with a little buffer
        print(" It is a right-angled triangle")
    elif sqrt_a_plus_b_power_two > c:
        print(" It is an acute triangle")
    else:
        print(" It is an obtuse triangle")

    a_plus_b_power_two = a**2 + b**2
    print(" a^2 + b^2 =", a_plus_b_power_two)

    c_power_two = c**2
    print(" c^2 =", c_power_two)

    if math.isclose(a_plus_b_power_two, c_power_two, rel_tol=epsilon):
        print(" It is a right-angled triangle")
    elif a_plus_b_power_two > c_power_two:
        print(" It is an acute triangle")
    else:
        print(" It is an obtuse triangle")

def main():
    a = float(input(" Enter the value of a: "))
    b = float(input(" Enter the value of b: "))
    c = float(input(" Enter the value of c: "))
    
    calculate_type(a, b, c)

if __name__ == "__main__":
    main()
