"""
Name:  Queues.py
Author:  Lee Brown
Created:  10/07/2020
Last Updated:  12/10/2020
Purpose:  This is to create a basic queue data structure.
Description:  This is going to create a class that can be used to create queue objects.  Even if there is a standard queue module in Python, I think that I should build my own.
     - If an opperation was successful, the method will return True or the relevant data.  Otherwise, it will return False.
     - The start of the stack is always at 0.  The end is wherever the end gets set.
"""
#nothing to import
def shiftArray(array):
    temp = [None] * len(array)
    for x in range(0, len(array)):
        temp[x] = array[x]
    for x in range(0, len(array) - 1):
        array[x + 1] = temp[x]
    return array

class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * self.size
        self.start = 0
        self.end = -1
    
    def enqueue(self, data):
        if(self.end > -1 and self.end != self.size - 1):
            self.queue = shiftArray(self.queue)
            self.queue[0] = data
            self.end = self.end + 1
            return True
        elif (self.end == -1):
            self.end = self.end + 1
            self.queue[self.end] = data
            return True
        else:
            #print("ERROR:  Queue Full.")
            return False
    
    def dequeue(self):
        if (self.end != -1):
            value = self.queue[self.end]
            self.queue[self.end] = None
            self.end = self.end - 1
            return value
        else:
            #print("ERROR:  Queue is empty.")
            return False

    
    def peek(self):
        if (self.end != 0):
            return self.queue[self.end]
        else:
            #print("ERROR:  Queue empty.")
            return False

    def isEmpty(self):
        if(self.end == -1):
            return True
        else:
            return False

    def isFull(self):
        if(self.end == self.size - 1):
            return True
        else:
            return False
    def getLength(self):
        return (self.end - self.start)
    
