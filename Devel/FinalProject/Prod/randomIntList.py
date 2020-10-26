"""
The idea of this program is to generate a list of random integers.  This list will have a specified length.

Author:  Lee Brown
Title: randomIntList.py
Details:  This program takes input values of length, startRange, and endRange.
          Length regulates how long the array should be, and the two range values
          indicate what possible range of values can be assigned to each index.
"""
import random

def randomIntList(length, startRange, endRange):
    intList = []
    for x in range(0, length):
        intList.append(random.randint(startRange, endRange))
    return intList
