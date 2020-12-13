"""
Name:  BubbleSort.py
Author:  Lee Brown
Created:  11/24/2020
Last Updated: 11/24/2020
Purpose:  A simple bubble sorting algorithm.  Nothing more, nothing less.
Description:  Takes in a list, sorts it, and returns the sorted result.
"""

def bubble_sort(unsorted_list):
    correct = len(unsorted_list)

    while(correct != 1):
        for x in range(0, correct - 1):
            if x == correct - 1:
                #if we are on the last index
                break
            elif unsorted_list[x] > unsorted_list[x + 1]:
                #if they  need to be swapped
                temp = unsorted_list[x]
                unsorted_list[x] = unsorted_list[x + 1]
                unsorted_list[x + 1] = temp
            else:
                #if nothing should be swapped
                pass
        correct -= 1
    return unsorted_list