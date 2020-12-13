from . import StackBuilder as stk
from . import PostfixExpressionGenerator as peg
from . import timer

"""
Helpful:
 - https://wiki.python.org/moin/HandlingExceptions

rules:
 - spaces must separate numbers
 - no spaces between /*-+^
"""
def solvePF(expression):

    #this first part makes a stack of numbers using my stack module
    numbers = stk.stack(len(expression))
    number = ""
    try:
        for x in expression:
            if(x == "0" or x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x == "9"):
                number = number + x
            elif(x == " "):
                numbers.push(number)
                number = ""
            elif(x == "+"):
                if(number != ""):
                    numbers.push(number)
                    number = ""
                t1 = numbers.pop()
                t2 = numbers.pop()
                result = int(t2)+int(t1)
                numbers.push(result)
            elif(x == "-"):
                if(number != ""):
                    numbers.push(number)
                    number = ""
                t1 = numbers.pop()
                t2 = numbers.pop()
                result = int(t2)-int(t1)
                numbers.push(result)
            elif(x == "^"):
                if(number != ""):
                    numbers.push(number)
                    number = ""
                t1 = numbers.pop()
                t2 = numbers.pop()
                result = int(t2)^int(t1)
                numbers.push(result)
            elif(x == "*"):
                if(number != ""):
                    numbers.push(number)
                    number = ""
                t1 = numbers.pop()
                t2 = numbers.pop()
                result = int(t2)*int(t1)
                numbers.push(result)
            elif(x == "/"):
                if(number != ""):
                    numbers.push(number)
                    number = ""
                t1 = numbers.pop()
                t2 = numbers.pop()
                result = int(t2)/int(t1)
                numbers.push(result)
            else:
                pass
        result = numbers.pop()
        if (numbers.getPointer() > -1):
            #print("ERROR:  Missing one or more signs in expression.")
            return False
        else:
            return result
    except TypeError:
        #print("ERROR:  Too many signs")
        return False
        
        
def test():
    time = timer()
    print(time.startTimer())
    expression = peg.genAddPFE(1000000)
    print(expression)
    result = solvePF(expression)
    print(result)
    print(time.endTimer())
