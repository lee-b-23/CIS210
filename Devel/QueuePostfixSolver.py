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

def solvePrefix(expression):
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numerals = ['0', '1','2','3','4','5','6','7','8','9','0']
    signQ = qz.Queue(len(expression))
    letters = qz.Queue(len(expression))

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
        print(letters.queue)
        print("x = " + str(x))
        if (x.lower() in alphabet):
            letters.enqueue(x)
        elif(x in numerals):
            temp = temp + str(x)
        else:
            if(temp != ''):
                letters.enqueue(temp)
            if(x != ' '):
                store = qz.Queue(letters.getLength() + 1)
                print(store.queue)
                for z in letters.queue:
                    if(z != None):
                        store.enqueue(z)
                value = len(letters.queue) - 1
                for y in range(0, letters.getLength()):
                    if(y != 0 and y != 1):
                        letters.dequeue()
                v1 = letters.dequeue()
                v2 = letters.dequeue()
                sign = signQ.dequeue()
                
                
                try:
                    print("AHGHDHGSJGH")
                    print("AHGJSFKHGJKLSF = " + str(x))
                    if(sign == "+"):
                        print("v1 = " + str(v1))
                        print("v2 = " + str(v2))
                        answer = int(v2) + int(v1)
                        print("answer = " + str(answer))
                        print("+")
                    elif(sign == "-"):
                        answer = int(v2) - int(v1)
                        print("-")
                    elif(sign == "*"):
                        answer = int(v2) * int(v1)
                        print("*")
                    elif(sign == "/"):
                        answer = int(v2) / int(v1)
                        print("/")
                    elif(sign == "^"):
                        answer = int(v2)**int(v1)
                        print("^")
                    else:
                        pass
                    print(store.queue)
                    for t in store.queue:
                        if(t != None):
                            print("OOF = " + str(t))
                            letters.enqueue(x)
                    letters.enqueue(answer)
                except:
                    if(sign == "+" or
                        sign == "-" or
                        sign == "/" or
                        sign == "^"):
                        answer = str(v2) + ' ' + str(v1) + sign
                    elif(sign == "*"):
                        answer = str(v2) + ' ' + str(v1) + sign
                    else:
                        pass
                    for x in store.queue:
                        if(x != None):
                            letters.enqueue(x)
                    letters.enqueue(answer)
                    
            temp = ''
    return letters.dequeue()
def main():
    wow = "1 5 + 3 25 -*"
    value = solvePrefix(wow)
    print(value)
main()
