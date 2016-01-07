import math


# def add(num1,num2,*therestnums):
#     new_num = 0
#     for i in therestnums:
#         i = int(i)
#         new_num = (int(new_num) + i)
#     return (int(num1)+int(num2)+int(new_num))

#next task: change functions to use reduce().
# we will want to convert both arguments into a list along with therestnums if it exists.
# the final function will look something like: reduce(lambda x,y: x-y, therestnums)

def add(num1,num2,*therestnums):
    new_num = 0
    for i in therestnums:
        i = int(i)
        new_num = (int(new_num) + i)
    return (int(num1)+int(num2)+int(new_num))

def subtract(num1, num2):
    return int(num1) - int(num2)


def multiply(num1, num2):
    return int(num1) * int(num2)


def divide(num1, num2):
    # Need to turn at least argument to float for division to
    # not be integer division
    return float(num1) / float(num2) 


def square(num1):
    # Needs only one argument
    return int(num1) * int(num1)


def cube(num1):
    # Needs only one argument
    return int(num1) * int(num1) * int(num1)


def power(num1, num2):
    #return int(num1) ** int(num2)  # ** = exponent operator
    if (num1 < 0 and type(num2) == float): 
        return ValueError
    num1 = float(num1)
    num2 = float(num2)
    return math.pow(num1,num2)

def mod(num1, num2):
    return int(num1) % int(num2)
