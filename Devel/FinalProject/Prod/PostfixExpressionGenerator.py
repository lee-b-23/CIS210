'''
sources:
 - source for meaning of word Operand: https://www.google.com/search?q=operand&oq=operand&aqs=chrome..69i57j69i61j69i60j0l4.834j0j7&sourceid=chrome&ie=UTF-8
'''
import random as r


def genPFE(num):
    #High chance of division by zero
    x = 0
    string = ""
    while (x < num - 1):
        string = string + str(r.randint(0, 10)) + " "
        x = x + 1
    string = string + str(r.randint(1, 10))
    for x in range(0, num - 1):
        sign = r.randint(0, 3)
        if sign == 3:
            string = string + "-"
        elif sign == 2:
            string = string + "+"
        elif sign == 1:
            string = string + "*"
        elif sign == 0:
            string = string + "/"
    return string

def genAddPFE(num):
    x = 0
    string = ""
    while (x < num - 1):
        string = string + str(r.randint(0, 10)) + " "
        x = x + 1
    string = string + str(r.randint(0, 10))
    for x in range(0, num - 1):
        string = string + "+"
    return string

    
def test():
    print(genAddPFE(10))
#test()
