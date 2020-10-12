"""
Name:  SolveInfix.py
Author:  Lee Brown
Created:  10/07/2020
Last Updated:  10/07/2020
Purpose:  Solving infix notation math problems(no exponents).
Description:
"""
import Queues
#the start variable will keep track of how far through the function is.
def solveInfix(start, expression):
    lastParen = 0
    parens = []
    for x in range(start, len(expression)):
        if(expression[x] == "(" or expression[x] == ")"):
            parens.append(expression[x])
    for x in range(start, len(expression)):
