"""
Name:  main.py
Author:  Lee Brown
Created:  10/2?/2020
Last Updated:  10/25/2020
Purpose:  The main menu module for my CIS210 final project.
Description:  This program will hold the user interface logic that interacts with
             and display my other modules.

Sources:
 - https://www.oreilly.com/library/view/arcpy-and-arcgis/9781783988662/ch02s06.html
"""
import sys
import ShowScreen as screen
from Prod import *

def main():
    error = 0
    
    screen.show_screen('welcome')
    
    while(True):
        #Test to see if incorrect input was found.  Display correct menu
        #accordingly.
        if(error == 0):
            value = screen.show_screen('main_menu')
        else:
            value = screen.show_screen('main_menu_incorrect')

        #Menu Options
        #timer
        if(value == '1'):
            error = 0
            value2 = ''
            while value2 != "e":
                t = timer.timer()
                value2 = screen.show_screen('timer_start')
                t.startTimer()
                value2 = screen.show_screen('timer_limbo')
                value = str(t.endTimer())
                value2 = screen.show_screen('timer_end', [['result', value]])

        #largest number
        elif(value == '2'):
            error = 0
            value2 = ''
            while(value2 != 'e'):
                input_judge = 0
                value2 = screen.show_screen('largest_num_start')
                if value2 != '':
                    value = value2.split(',')

                    counter = 0
                    for x in range(0, len(value)):
                        value[x] = value[x].strip()
                        try:
                            value[x] = int(value[x])
                        except:
                            input_judge = 1
                    if input_judge != 0:
                        #if they typed something wrong
                        value2 = screen.show_screen('largest_num_incorrect')
                    else:
                        data = LargestNum.largestNum(value, [])[0]
                        value2 = screen.show_screen('largest_num_end', [['<num>', str(data)]])
                else:
                    value = randomIntList.randomIntList(100, -100, 100)
                    data = LargestNum.largestNum(value, [])[0]
                    value2 = screen.show_screen('largest_num_end', [['<num>', str(data)]])

        elif(value == '3'):
            error = 0
            value2 = ''
            
            while(value2 != 'e'):
                value = screen.show_screen('postfix_start')
                data = str(PostfixSolver.solvePF(value))
                value2 = screen.show_screen('postfix_end', [['<result>', data]])
        
        elif(value == '4'):
            error = 0
        elif(value == '5'):
            error = 0
        elif(value == '6'):
            error = 0
            screen.show_screen('about')
        elif(value == '7'):
            break
        else:
            #incorrect input option
            error = 1
    screen.show_screen('exit')
main()
