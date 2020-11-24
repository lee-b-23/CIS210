"""
Name:  BubbleSortAnimation.py
Author:  Lee Brown
Created:  11/18/2020
Last Updated:  11/24/2020
Purpose:  This is to animate the process of bubble sorting.
Description:
Sources:
   The following are helpful sources that I used...
    - https://stackoverflow.com/questions/12822762/pylab-ion-in-python-2-matplotlib-1-1-1-and-updating-of-the-plot-while-the-pro
    - https://stackoverflow.com/questions/29428987/python-matplotlib-update-graph-without-closing-window
    - https://stackoverflow.com/questions/11140787/closing-pyplot-windows
    - https://www.kite.com/python/answers/how-to-clear-a-plot-in-matplotlib-in-python
    - https://stackoverflow.com/questions/18973404/setting-different-bar-color-in-matplotlib-python
    - https://docs.python.org/3/library/winsound.html
    - https://www.geeksforgeeks.org/python-winsound-module/
    - https://icolorpalette.com/color/python-yellow
    - https://icolorpalette.com/color/python-blue
    - https://www.hexcolortool.com/#808080
"""
import matplotlib.pyplot as plt
import winsound as sound
import randomIntList as rand

def bubble_animation(unsorted_list):
    #Sets initialization stuff: (1) Makes the plot so that it can does not block code execution, (2) gets the length of the list, (3) sets x-axis permanent values.
    plt.ion()
    correct = len(unsorted_list)
    x_axis = []
    for x in range(0, correct):
        x_axis.append(str(x))
    
    #this is to redraw the plot for every update.  It: Sets the axis labels, sets the title with the current swap and check count, populates the graph, draws it, and pauses.
    def update_plot(y_values, x_cur, checks, swaps, correct):
        plt.clf()
        plt.xlabel("Indexes in the List")
        plt.ylabel("Values")
        plt.title("Bubble-Sorting a List\nList Size = " + str(len(unsorted_list)) + "\nchecks = " + str(checks) + " | swaps = " + str(swaps))
        plot = plt.bar(x_axis, y_values, color="#808080")
        
        for index in range(correct, len(unsorted_list)):
            plot[index].set_color('#3776ab')
        plot[x_cur].set_color('#ffd343')
        plot[x_cur + 1].set_color('#ffd343')
        plt.draw()
        plt.pause(0.00001)
    
    swaps = 0
    checks = 0
    update_plot(unsorted_list, 0, 0, 0, correct)
    while(correct != 1):
        for x in range(0, correct - 1):
            update_plot(unsorted_list, x, checks, swaps, correct)
            checks += 1
            if x == correct - 1:
                #if we are on the last index
                break
            elif unsorted_list[x] > unsorted_list[x + 1]:
                swaps += 1
                #if they  need to be swapped
                temp = unsorted_list[x]
                unsorted_list[x] = unsorted_list[x + 1]
                unsorted_list[x + 1] = temp
                #sound.PlaySound('swap.wav', sound.SND_FILENAME)
            else:
                #if nothing should be swapped
                pass
        correct -= 1
    plt.clf()
    plt.title("Bubble-Sorting a List\nList Size = " + str(len(unsorted_list)) + "\nchecks = " + str(checks) + " | swaps = " + str(swaps))
    plt.xlabel("Indexes in the List")
    plt.ylabel("Values at a Given Index")
    plt.bar(x_axis, unsorted_list, color="#3776ab")
    plt.draw()
    plt.pause(5)
    return unsorted_list

if __name__ == '__main__':
    unsorted_list = rand.randomIntList(100, 0, 50)
    print(unsorted_list)
    value = bubble_animation(unsorted_list)
    print(value)