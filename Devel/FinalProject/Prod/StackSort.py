"""
Name:  StackSort.py
Author:  Lee Brown
Created:  10/29/2020
Last Updated:  10/29/2020
Purpose:  Sorts a list of values using stacks.
Description:  Instead of employing traditional lists, this sorting method uses
            three stacks.
Outline:

def sort_using_stacks(original list):
    turn original list into a stack
    make another stack2
    make a stack3 as well
    while stack2 and stack3 are not empty:
        put top item of stack into stack2

        while True:
            pull out next item
            if that item is less than the top item of stack2, 
                add it to stack3
            else 
                swap this item with the top of stack2
                put everything from stack3 back into stack
            if stack is empty:
                put stack 3 back into stack
                break
"""
import Prod.StackBuilder as stacks

def stack_sort(num_list):
    stack1 = stacks.stack(len(num_list))
    stack2 = stacks.stack(len(num_list))
    stack3 = stacks.stack(len(num_list))

    #add all list items to the first stack
    for x in num_list:
        stack1.push(x)

    while stack1.getPointer() > 0:
        stack2.push(stack1.pop())


        #until the one value has been added to stack2 and has been compared to all other potential values
        while(True):
            next_item = stack1.pop()
            if next_item < stack2.peek():
                stack3.push(next_item)
            else:
                temp = stack2.pop()
                stack2.push(next_item)
                stack1.push(temp)
            if stack1.isEmpty():
                if stack3.isEmpty() == False:
                    while stack3.isEmpty() == False:
                        value = stack3.pop()
                        stack1.push(value)
                else:
                    stack2.push(stack3.pop())
                break
    
    stack2.push(stack1.pop())
    return stack2.stack