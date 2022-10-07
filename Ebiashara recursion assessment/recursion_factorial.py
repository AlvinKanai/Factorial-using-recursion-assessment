"""
Python program to calculate Factorial using recursion

Recursion: Technique of making a function call itself to solve a computational problem.

Factorial: Product of all positive integers less than or equal to a given positive integer and denoted by that integer and an exclamation point eg. 5!
"""


def recursion_factorial(num):
    # checking whether the provided integer is 1 or 0
    if num == 0 or num == 1:
        return 1
    else:
        return num*recursion_factorial(num-1)


# user input
num = int(input("Enter a number: "))

# output and validation
if num < 0:
    print("There's no factorial for negative numbers")
else:
    # calling the function
    print("The factorial of ", num, "is ", recursion_factorial(num))
