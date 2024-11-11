# Caleb Egbert
# UWYO COSC 1010
# November 10, 2024
# Lab 08
# Lab Section: 12
# Sources, people worked with, help given to: TA
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
def convert_to_number(s):
    try:
        if '.' in s:
            if s.count('.') == 1:
                return float(s)
            else:
                return False
        else:
            return int(s)
    except ValueError:
        return False

print("*" * 75)


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false

# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list
def slope_intercept(m, b, lower_x, upper_x):
    if not (isinstance(lower_x, int) and isinstance(upper_x, int)) or lower_x > upper_x:
        return False
    y_values = []
    for x in range(lower_x, upper_x + 1):
        y = m * x + b
        y_values.append(y)
    return y_values

while True:
    m = input("Enter slope (m), or type 'exit' to quit: ")
    if m.lower() == 'exit':
        break
    b = input("Enter y-intercept (b): ")
    lower_x = input("Enter lower x bound: ")
    upper_x = input("Enter upper x bound: ")
    
    m = convert_to_number(m)
    b = convert_to_number(b)
    lower_x = convert_to_number(lower_x)
    upper_x = convert_to_number(upper_x)
    
    if m is not False and b is not False and isinstance(lower_x, int) and isinstance(upper_x, int):
        print(slope_intercept(m, b, lower_x, upper_x))
    else:
        print("Invalid input. Please enter valid numbers.")


print("*" * 75)

import math

def safe_sqrt(n):
    if n < 0:
        return None
    return math.sqrt(n)

def quadratic_solver(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    sqrt_discriminant = safe_sqrt(discriminant)
    if sqrt_discriminant is None:
        return None 
    x1 = (-b + sqrt_discriminant) / (2 * a)
    x2 = (-b - sqrt_discriminant) / (2 * a)
    return x1, x2


while True:
    a = input("Enter coefficient a, or type 'exit' to quit: ")
    if a.lower() == 'exit':
        break
    b = input("Enter coefficient b: ")
    c = input("Enter coefficient c: ")
    
    a = convert_to_number(a)
    b = convert_to_number(b)
    c = convert_to_number(c)
    
    if a is not False and b is not False and c is not False:
        roots = quadratic_solver(a, b, c)
        if roots:
            print(f"The roots are: {roots[0]} and {roots[1]}")
        else:
            print("No real roots.")
    else:
        print("Invalid input. Please enter valid numbers.")

# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null
