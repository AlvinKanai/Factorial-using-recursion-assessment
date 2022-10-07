"""
Problem: Python program to calculate Factorial using recursion

Recursion: Technique of making a function call itself to solve a computational problem.

Factorial: Product of all positive integers less than or equal to a given positive integer and denoted by that integer and an exclamation point eg. 5!
"""


def recursion_factorial(num):
    # Base case: Checking whether the provided integer is 1 or 0
    if num == 0 or num == 1:
        return 1

    else:
        # recursive case
        return num*recursion_factorial(num-1)


# code execution when file is run as a script
if __name__ == '__main__':
    try:
        # user input of type integer
        num = int(input("Enter a number: "))
    except ValueError:
        raise Exception('The input is not a valid integer')

    #  Error handing for negative numbers
    if num < 0:
        raise Exception("Factorial for negative numbers does not exist")

    # output and validation
    try:
        # calling the function
        print("The factorial of ", num, "is ", recursion_factorial(num))
    except:
        # handles stack overflow error
        raise Exception("Number is too large")
