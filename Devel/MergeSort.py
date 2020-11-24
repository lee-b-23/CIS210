"""
Name:  MergeSort.py
Author:  Lee Brown
Created:  11/24/2020
Last Updated:  11/24/2020
Purpose:  Create a Python merge sort algorithm to compare to other sorting algorithms.
Description:  Dito ^
Sources:
 - https://www.interviewbit.com/tutorial/merge-sort-algorithm/
 - https://www.kite.com/python/answers/how-to-split-a-list-in-half-in-python#:~:text=Call%20len(iterable)%20with%20iterable,second%20half%20of%20the%20list.
Outline:
    I.  Take original list.
    II.  if possible, divide that into two
    III.  If step two succeeded, repeat steps 1 and 2 on the new split lists.
    IV.  Make a results list
    V.  Take the two sublists and combine them by comparing the first values and emptying them like stacks into the results list.
    VI.  Return the results list.
Pseudocode:
    import my stack builder
    def merge_sort(unsorted_list):
        list1 = first half of unsorted_list
        list2 = second half of unsorted_list
        if length of list1 > 1:
            list1 = merge_sort(list1)
        if length of list2 > 1:
            list2 = merge_sort(list2)
        
        if len(list1) > len(list2):
            iterations of the for loop = len(list1)
        else:
            iterations of the for loop = len(list2)
        
        add list1 and list2 to two stacks
        results_list = []
        i = 0
        j = 0
        while True:
            try:
                if list1[i] < list2[j]:
                    append list1[i] to results_list
                    i += 1
                else:
                    append list2[j] to the results_list
                    j += 1
            except:
                while list1 still has values that are yet to be added:
                    add those values
                while list2 still has values that are yet to be added:
                    add those values
                break

"""
import randomIntList as rand

def merge_sort(unsorted_list):
    #gets half of the list length and splits the list into two
    len1 = int(len(unsorted_list)/2)
    list1 = unsorted_list[:len1]
    list2 = unsorted_list[len1:]

    #recursive calls to further split the list
    if len(list1) > 1:
        list1 = merge_sort(list1)
    if len(list2) > 1:
        list2 = merge_sort(list2)
    
    #take solutions from recursion and merge them
    result = []
    i = 0
    j = 0
    while True:
        try:
            if list1[i] < list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        except:
            while i < len(list1):
                result.append(list1[i])
                i += 1
            while j < len(list2):
                result.append(list2[j])
                j += 1
            break
    return result

if __name__ == '__main__':
    ints = rand.randomIntList(11, 1, 999)
    print("original list:  " + str(ints))
    print("sorted list:  " + str(merge_sort(ints)))