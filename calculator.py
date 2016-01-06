"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here

#do_setup()


# while (exit_condition_not_reached == True):
#     input = consume_input()
#     output = evaluate_input(input)
#     print output

while True: 
    input = raw_input(">")
    input_list = input.split(" ")
    if input_list[0] == "+":
        add(input_list[1],input_list[2])
    elif input_list[0] == "-":
        subtract(input_list[1],input_list[2])   
    elif input_list[0] == "*":
        multiply(input_list[1],input_list[2])
    elif input_list[0] == "/":
        divide(input_list[1],input_list[2])
    elif input_list[0] == "square":
        square(input_list[1])   
    elif input_list[0] == "cube":
        cube(input_list[1])
    elif input_list[0] == "pow":
        power(input_list[1],input_list[2])
    elif input_list[0] == "mod": 
        mod(input_list[1],input_list[2])
    elif input_list[0] == "q":
        return False
            


# def do_setup():
#     pass

# def exit_condition_not_reached(input):
#     input_list = consume_input(input)
#     if input_list[0] == "q":
#         return False


# def consume_input(input):
#     input = raw_input(">")
#     split_input = input.split(" ")
#     return split_input 

# def evaluate_input(input):
#     input_list = consume_input(input)
#     if input_list[0] == "+":
#         add(input_list[1],input_list[2])
#     elif input_list[0] == "-":
#         subtract(input_list[1],input_list[2])   
#     elif input_list[0] == "*":
#         multiply(input_list[1],input_list[2])
#     elif input_list[0] == "/":
#         divide(input_list[1],input_list[2])
#     elif input_list[0] == "square":
#         square(input_list[1])   
#     elif input_list[0] == "cube":
#         cube(input_list[1])
#     elif input_list[0] == "pow":
#         power(input_list[1],input_list[2])
#     elif input_list[0] == "mod":
#         mod(input_list[1],input_list[2])
    




    

