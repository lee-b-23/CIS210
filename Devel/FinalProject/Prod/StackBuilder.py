"""
Name:  StackBuilder
Author:  Lee Brown
Created:  9/16/2020
Last Updated:  12/10/2020
Purpose:  The class defined here will allow for the creation of a stack object.
Description:  This class creates a last-in-first-out (LIFO) data container known
            as a stack.  The calling module can push values onto the stack, pop
            them off of it, peek at the top value, get the top value position,
            and see if the list is empty.
Sources:
 - Empty List Idea:  https://stackoverflow.com/questions/10712002/create-an-empty-list-in-python-with-certain-size
"""

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
            pass
            #print("ERROR:  Stack overflow error.")
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
            #print("ERROR:  Stack is empty.")
            return None
    def printStack(self):
        print(self.stack)
    def isEmpty(self):
        if self.pointer == -1:
            return True
        else:
            return False
    def isFull(self):
        if self.pointer == len(self.stack) - 1:
            return True
        else:
            return False
