''' 
The calculator has two function:
Calculator:
This function call the infix_to post_it module who can convert a infix expression into and postfix(polish inverse)
In the result  every string in array that is a number is convert in a integer before call the second function that is compute().

Compute:
this function takes the postfix expression and performs the calculation for return it.
The deque structure allows to stack operations to interpret a sequence written in inverse polonaise notation:
numbers (here integers) are simply stacked with the .append() operation;
operators (here strings) unstack with the .pop() operation the last two values of the stack, evaluate the operation and stack the result.


'''  
from collections import deque

import math
from infix_to_postfix import *
from convert_expression import *


def calculator(infix_expression):

    infix_expression=convert(infix_expression)
    tokens = tokenize(infix_expression)
    postfixexpression=" ".join(shunt(tokens))
    # create and array with every element of postfix expression
    # print(postfixexpression)
    return calculate(postfixexpression)
    


def calculate(expression):
  
    print(expression)
    # Create a stack to hold the operands
    stack = []

    # Define the postfix expression
    

    # Iterate over the expression
    for token in expression.split():
        # If the token is an operand, convert it to an integer and push it onto the stack
        if token.isdigit():
            stack.append(int(token))
            print(f'stack antes: {stack}')
        else:
            # If the token is an operator, pop the top two items from the stack,
            # apply the operator, and push the result back onto the stack
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = 0
            if token == "+":
                result = operand1 + operand2
            elif token == "-":
                result = operand1 - operand2
            elif token == "*":
                result = operand1 * operand2
            elif token == "/":
                result = operand1 / operand2
            elif token == "%":
                result = operand1 % operand2
            elif token == "C":
                result = math.cos(operand2)
            elif token == "S":
                result = math.sin(operand2)
            elif token == "T":
                result = math.tan(operand2)
            
            elif token == "#":
                operand1=1
                result = math.sqrt(operand2)
            stack.append(result)
            print(f'stack despues: {stack}')

    # When the loop is finished, the final result will be the top item on the stack
    result = stack.pop()
    print(result)
    return result



# calculate('2 -2 * 1 -')
