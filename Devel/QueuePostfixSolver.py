"""
Name:  PostfixQSolver.py
Author:  Lee Brown
Created:  10/11/2020
Last Updated:  10/11/2020
Purpose:  This code will solve postfix expressions with the help of queues.
Description:

Outline:
I.  Fill up queue with signs.
II.  Use a similar stack approach to collect the letters and numbers
"""
import Queues as qz
import StackBuilder as stk

def solvePrefix(expression):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numerals = ['0', '1','2','3','4','5','6','7','8','9','0']
    signQ = qz.Queue(len(expression))
    letters = stk.stack(len(expression))

    x = 0
    while(x < len(expression)):
        if(expression[x] == "*" or
           expression[x] == "-" or
           expression[x] == "+" or
           expression[x] == "/" or
           expression[x] == "^"):
            signQ.enqueue(expression[x])
        else:
            pass
        x = x + 1
    temp = ''
    for x in expression:
        #print("x = " + str(x))
        if (x.lower() in alphabet):
            letters.push(x)
        elif(x in numerals):
            temp = temp + str(x)
        else:
            if(temp != ''):
                letters.push(temp)
            if(x != ' '):
                v1 = letters.pop()
                v2 = letters.pop()

                sign = signQ.dequeue()
                try:
                    if(sign == "+"):
                        answer = int(v2) + int(v1)
                    elif(sign == "-"):
                        answer = int(v2) - int(v1)
                    elif(sign == "*"):
                        answer = int(v2) * int(v1)
                    elif(sign == "/"):
                        answer = int(v2) / int(v1)
                    elif(sign == "^"):
                        answer = int(v2)**int(v1)
                    else:
                        pass
                    letters.push(answer)
                except:
                    if(sign == "+" or
                        sign == "-" or
                        sign == "/" or
                        sign == "^"):
                        answer = str(v2) + ' ' + str(v1) + sign
                    elif(sign == "*"):
                        answer = str(v2) + ' ' + str(v1) + sign
                    print("EXCEPTION")
                    letters.push(answer)
                        
            temp = ''
    return letters.pop()
def main():
    wow = "1 5 + 3 25 -*"
    value = solvePrefix(wow)
    print(value)
main()
