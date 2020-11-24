"""
Name:  sort_timing.py
Author:  Lee Brown
Created:  11/23/2020
Last Updated:  11/24/2020
Purpose:  Testing the sorting times for various sorting methods.
Description:  This will employ three sets of data which will be sorted through by two algorithims, the bubble-sorting and another method.
Outline:
    do all of the necessary imports
    def main():
        create three sets of data using my random integer generator (1000, 100000, and 20000 items respectively)
        
        start a timer
        first sorting algorithm on first data set
        end timer and store result

        start a timer
        second sorting algorithm on first data set
        end timer and store result

        start a timer
        first sorting algorithm on second data set
        end timer and store result

        start a timer
        second sorting algorithm on second data set
        end timer and store result

        start a timer
        first sorting algorithm on third data set
        end timer and store result

        start a timer
        second sorting algorithm on third data set
        end timer and store result

        display the final results neatly
Sources:
 - https://www.interviewbit.com/tutorial/sorting-algorithms/#sorting-algorithms
"""
import randomIntList as rand
import BubbleSort as bubble
import MergeSort as merge
import timer

if __name__ == '__main__':
    #the tests are saved in the results list in the order that they were completed.  The list contains the times for each test.
    data = [[],[], []]
    totals = [1000, 100000, 20000]
    test_lengths = [100, 1000, 20000]      #<<<<<THIS IS TO TEST THE FINAL DISPLAY WITHOUT HAVING TO WAIT A LONG TIME
    results = [None] * 6
    time = timer.timer()

    #create the starting lists
    for x in range(0, 3):
        data[x] = rand.randomIntList(totals[x], 1, 999)
    
    

    #data set 1
    #bubble sort
    time.startTimer()
    r = bubble.bubble_sort(data[0])
    results[0] = time.endTimer()
    #merge Sort
    time.startTimer()
    r = merge.merge_sort(data[0])
    results[1] = time.endTimer()


    #data set 2
    #bubble sort
    time.startTimer()
    r = bubble.bubble_sort(data[1])
    results[2] = time.endTimer()
    #merge Sort
    time.startTimer()
    r = merge.merge_sort(data[1])
    results[3] = time.endTimer()


    #data set 3
    #bubble sort
    time.startTimer()
    r = bubble.bubble_sort(data[2])
    results[4] = time.endTimer()
    #merge sort
    time.startTimer()
    r = merge.merge_sort(data[2])
    results[5] = time.endTimer()



    #DISPLAY RESULTS
    print("------------FINAL RESULTS------------")
    count = 1
    for result in results:
        print("Test " + str(count) + ":  time = " + str(result))
        count += 1