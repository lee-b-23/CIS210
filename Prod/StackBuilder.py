'''
Name:  StackBuilder
Author:  Lee Brown
Date:  9/16/2020
Purpose:  The class defined here will allow for the creation of a stack object.

Sources:
 - Empty List Idea:  https://stackoverflow.com/questions/10712002/create-an-empty-list-in-python-with-certain-size
'''

class stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * self.size
        self.top = self.size-1
        self.bottom = 0
        self.pointer = -1
    def getPointer(self):
        return self.pointer
    def peek(self):
        return self.stack[self.pointer]
    def push(self, value):
        if(self.pointer == self.top):
            print("ERROR:  Stack overflow error.")
        else:
            self.pointer = self.pointer + 1
            self.stack[self.pointer] = value
    def pop(self):
        if(self.pointer >= 0):
            pop = self.stack[self.pointer]
            self.stack[self.pointer] =  None
            self.pointer = self.pointer - 1
            return pop
        else:
            print("ERROR:  Stack is empty.")
            return None
    def printStack(self):
        print(self.stack)

def test():
    s = stack(10)
    print("<<<Pushing Values>>>")
    print(s.getPointer())
    s.push(10)
    print(s.getPointer())
    s.push(9)
    print(s.getPointer())
    s.push(8)
    print(s.getPointer())
    s.push(7)
    print(s.getPointer())
    s.push(6)
    print(s.getPointer())
    s.push(5)
    print(s.getPointer())
    s.push(4)
    print(s.getPointer())
    s.push(3)
    print(s.getPointer())
    s.push(2)
    print(s.getPointer())
    s.push(1)
    print(s.getPointer())
    #s.push(0)

    print("")
    print("<<<Stack>>>")
    s.printStack()
    print("Top = " + str(s.peek()))

    print("")
    print("<<<Popping Values>>>")
    print(s.pop())
    print(s.pop())
    s.printStack()
    print(s.getPointer())
#test()
