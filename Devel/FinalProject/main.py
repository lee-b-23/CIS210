"""
Name:  main.py
Author:  Lee Brown
Created:  10/2?/2020
Last Updated:  12/06/2020
Purpose:  The main menu module for my CIS210 final project.
Description:  This program will hold the user interface logic that interacts with
             and display my other modules.

Sources:
 - https://www.oreilly.com/library/view/arcpy-and-arcgis/9781783988662/ch02s06.html
"""
import sys
import traceback            #<debugging only
import ShowScreen
from Prod import *

def wrap_lines(string, num_lines, chars_per_line):
    count = 0
    temp_line = ''
    return_data = []
    for character in string:
        if count == chars_per_line:
            return_data.append(temp_line)
            temp_line = ''
            count = 0
        temp_line += character
        count += 1
        if len(return_data) == num_lines:
            break
    if len(return_data) < num_lines and len(temp_line) > 0:
        return_data.append(temp_line)
    for x in range(len(return_data), num_lines):
        return_data.append('')
    return return_data

def main():
    error = 0
    
    screen = ShowScreen.ShowScreen('screens', '.txt')
    screen.show_screen('static', 'welcome')
    
    while(True):
        #Test to see if incorrect input was found.  Display correct menu
        #accordingly.
        if(error == 0):
            value = screen.show_screen('static', 'main_menu')
        else:
            value = screen.show_screen('static', 'main_menu_incorrect')

        #Menu Options
        #timer
        if(value == '1'):
            error = 0
            value2 = ''
            while value2 != "e":
                t = timer.timer()
                value2 = screen.show_screen('static', 'timer_start')
                t.startTimer()
                value2 = screen.show_screen('static', 'timer_limbo')
                value = str(t.endTimer())
                value2 = screen.show_screen('static', 'timer_end', ['result'], [value])

        #largest number
        elif(value == '2'):
            error = 0
            value2 = ''
            while(value2.strip().lower() != 'e'):
                input_judge = 0
                value2 = screen.show_screen('static', 'largest_num_start')
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
                        value2 = screen.show_screen('static', 'largest_num_incorrect')
                    else:
                        data = LargestNum.largestNum(value, [])[0]
                        value2 = screen.show_screen('static', 'largest_num_end', ['<num>'], [str(data)])
                else:
                    value = randomIntList.randomIntList(100, -100, 100)
                    data = LargestNum.largestNum(value, [])[0]
                    value2 = screen.show_screen('static', 'largest_num_end', ['<num>'], [str(data)])


        #OPTION 3, Postfix solver
        elif(value == '3'):
            error = 0
            value2 = ''
            
            #main loop
            while(value2 != 'e'):
                value = screen.show_screen('static', 'postfix_start')
                data = str(PostfixSolver.solvePF(value))
                value2 = screen.show_screen('static', 'postfix_end', ['<result>'], [data])
        


        #OPTION 4, factors of three from list (same format as the largest number finder, even copied the code from it :))
        elif(value == '4'):
            error = 0

            value2 = ''
            #main loop
            while(value2.strip().lower() != 'e'):
                input_judge = 0
                value2 = screen.show_screen('static', 'three_factors_start')
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
                        value2 = screen.show_screen('static', 'largest_num_incorrect')
                    else:
                        data = threeFactors.threeFactors(value)
                        temp_data = str(data)
                        display_data = []
                        display_tags = ['<num1>', '<num2>', '<num3>', '<num4>', '<num5>', '<num6>', '<num7>']

                        #this creates a list of lines to display the list of numbers neatly on the page.
                        display_data = wrap_lines(temp_data, 7, 18)
                        if ']' not in display_data[6] and display_data[6] != '':
                            value2 = screen.show_screen('static', 'three_factors_end_large', display_tags, display_data)
                        else:
                            value2 = screen.show_screen('static', 'three_factors_end', display_tags, display_data)
                else:
                    value = randomIntList.randomIntList(100, -100, 100)
                    data = threeFactors.threeFactors(value)
                    temp_data = str(data)
                    display_data = []
                    display_tags = ['<num1>', '<num2>', '<num3>', '<num4>', '<num5>', '<num6>', '<num7>']
                    #this creates a list of lines to display the list of numbers neatly on the page.
                    display_data = wrap_lines(temp_data, 7, 18)
                    if ']' not in display_data[6] and display_data[6] != '':
                        value2 = screen.show_screen('static', 'three_factors_end_large', display_tags, display_data)
                    else:
                        value2 = screen.show_screen('static', 'three_factors_end', display_tags, display_data)



        #OPTION 5, Random Integer list
        elif(value == '5'):
            value2 = ''
            error = 0
            
            bad = False
            #main loop
            while(value2.strip().lower() != 'e'):
                value2 = screen.show_screen('static', 'random_ints_start')

                #see if their answer is formatted correctly, and if so, do something with it
                try:
                    data = value2.split(',')
                    if len(data) != 3:
                        bad = True
                    data[0] = int(data[0])
                    data[1] = int(data[1])
                    data[2] = int(data[2])
                    
                    data = str(randomIntList.randomIntList(data[0], data[1], data[2])).strip()
                    display_tags = ['<l1>', '<l2>', '<l3>', '<l4>', '<l5>', '<l6>', '<l7>', '<l8>', '<l9>', '<l10>']
                    display_data = wrap_lines(data, 10, 56)
                    if len(display_data[-1]) != 0 and ']' not in display_data[-1]:
                        value2 = screen.show_screen('static', 'random_ints_end_large', display_tags, display_data)
                    else:
                        value2 = screen.show_screen('static', 'random_ints_end', display_tags, display_data)

                except:
                    value2 = screen.show_screen('static', 'random_ints_incorrect')
                    

        #OPTION 6, Bubble Sorting
        elif(value == '6'):
            error = 0
            value2 = ''
            #main loop
            while(value2.strip().lower() != 'e'):
                input_judge = 0
                value2 = screen.show_screen('static', 'bubble_sort_start')
                animation = screen.show_screen('static', 'bubble_sort_animation_prompt')
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
                        value2 = screen.show_screen('static', 'bubble_sort_start_incorrect')
                    else:
                        display_tags = ['<l1>', '<l2>', '<l3>', '<l4>', '<l5>', '<l6>', '<l7>']
                        if animation.lower().strip() == 'y' or animation.lower().strip() == 'yes':
                            #There is an error when the user exits the pyplot window manually instead of letting it close itself
                            try:
                                data = BubbleSortAnimation.bubble_animation(value)
                            except:
                                data = BubbleSort.bubble_sort(value)
                            
                            data = str(data)
                            display_data = wrap_lines(data, 7, 43)
                            value2 = screen.show_screen('static', 'bubble_sort_end', display_tags, display_data)
                        else:
                            data = BubbleSort.bubble_sort(value)
                            data = str(data)
                            display_data = wrap_lines(data, 7, 43)
                            value2 = screen.show_screen('static', 'bubble_sort_end', display_tags, display_data)
                else:
                    #if they choose a random list
                    display_tags = ['<l1>', '<l2>', '<l3>', '<l4>', '<l5>', '<l6>', '<l7>']

                    if animation.lower().strip() == 'y' or animation.lower().strip() == 'yes':
                        try:
                            ints = randomIntList.randomIntList(20, 1, 20)
                            data = BubbleSortAnimation.bubble_animation(ints)
                        except:
                            data = BubbleSort.bubble_sort(ints)
                        
                        data = str(data)
                        display_data = wrap_lines(data, 7, 43)
                        value2 = screen.show_screen('static', 'bubble_sort_end', display_tags, display_data)
                    else:
                        data = BubbleSort.bubble_sort(randomIntList.randomIntList(20, 1, 20))
                        data = str(data)
                        display_data = wrap_lines(data, 7, 43)
                        value2 = screen.show_screen('static', 'bubble_sort_end', display_tags, display_data)



        #OPTION 7, Prime Number Finder
        elif(value == '7'):
            error = 0
            value2 = ''

            while(value2.strip().lower() != 'e'):
                value2 = screen.show_screen('static', 'primes_start')

                try:
                    display_tags = ['<l1>', '<l2>', '<l3>', '<l4>', '<l5>', '<l6>', '<l7>', '<l8>', '<l9>', '<l10>', '<l11>', '<num>']
                    data = int(value2)
                    data2 = FindPrimes.return_x_primes(data)
                    display_data = wrap_lines(str(data2), 11, 45)
                    display_data.append(value2)

                    if ']' not in display_data[-1] and display_data[-1] != '':
                        value2 = screen.show_screen('static', 'primes_end_large', display_tags, display_data)
                    else:
                        value2 = screen.show_screen('static', 'primes_end', display_tags, display_data)
                except:
                    value2 = screen.show_screen('static', 'primes_start_incorrect')



        #OPTION 8, Factor Checker
        elif(value == '8'):
            error = 0
            value2 = ''

            while(value2.strip().lower() != 'e'):
                too_large = False
                value2 = screen.show_screen('static', 'factor_check_start')

                data = value2.split(',')
                try:
                    display_data = []
                    display_tags = ['<num1>', '<answer>', '<num2>']
                    if len(data) != 2:
                        raise Exception()
                    data[0] = int(data[0].strip())
                    data[1] = int(data[1].strip())
                    
                    if data[0] > 9999999999999998 or data[1] > 9999999999999998:
                        too_large = True
                        raise ValueError

                    data2 = IsFactor.is_factor(data[1], data[0])
                    display_data.append(str(data[0]))
                    if data2:
                        display_data.append('IS a factor of')
                    else:
                        display_data.append('IS NOT a factor of')
                    display_data.append(str(data[1]))

                    value2 = screen.show_screen('static', 'factor_check_end', display_tags, display_data)
                except:
                    if too_large:
                        value2 = screen.show_screen('static', 'factor_check_start_toolarge')
                    else:
                        value2 = screen.show_screen('static', 'factor_check_start_incorrect')



        #OPTION 9, Queue Builder
        elif(value == '9'):
            #This calculates how many spaces should go before the queue in the screen based on the queue's size.
            def add_spaces(the_queue):
                spaces = int((72 - len(str(queue.queue)))/2)
                print_queue = ''
                for x in range(0, spaces):
                    print_queue += ' '
                print_queue += str(queue.queue)
                return print_queue
            error = 0
            value2 = ''

            #main loop
            while(value2.strip().lower() != 'e'):
                size = True
                value2 = screen.show_screen('static', 'queues_start')
                try:
                    #input testing block
                    queue_size = int(value2)
                    if queue_size < 1 or queue_size > 9:
                        size = False
                        raise Exception()
                    
                    #create queue
                    queue = Queues.Queue(queue_size)

                    #action completion loop
                    while(value2.strip().lower() != 'e'):
                        action = ''
                        print_queue = add_spaces(queue.queue)
                        value2 = screen.show_screen('static', 'queues_action', ['<queue>'], [print_queue])
                        try:
                            #test the input to see if it is an int and if it is in the menu
                            value2 = int(value2)
                            if value2 not in [1, 2, 3, 4, 5, 6]:
                                raise Exception()
                            
                            #action options
                            if value2 == 1:
                                #limit input to 4 characters for queue
                                size_error = False
                                while(True):
                                    if not size_error:
                                        print_queue = add_spaces(queue.queue)
                                        value2 = screen.show_screen('static', 'queues_action_enqueue', ['<queue>'], [print_queue])
                                    else:
                                        value2 = screen.show_screen('static', 'queues_action_enqueue_incorrect')
                                    if len(value2) > 4:
                                        pass
                                    else:
                                        break
                                try_enqueue = queue.enqueue(value2)
                                if not try_enqueue:
                                    action = 'Unable to enqueue.  Queue full.'
                                else:
                                    action = 'Enqueue completed successfully!'
                            elif value2 == 2:
                                try_dequeue = queue.dequeue()
                                if not try_dequeue:
                                    action = 'Unable to dequeue.  Queue empty.'
                                else:
                                    action = 'Dequeued ' + str(try_dequeue) + ' successfully!'
                            elif value2 == 3:
                                try_peek = queue.peek()
                                if not try_peek:
                                    action = 'Unable to peek.  Queue is empty.'
                                else:
                                    action = 'The top value is: ' + str(try_peek)
                            elif value2 == 4:
                                try_empty = queue.isEmpty()
                                if try_empty:
                                    action = 'The queue is empty.'
                                else:
                                    action = 'The queue is not empty.'
                            elif value2 == 5:
                                try_empty = queue.isFull()
                                if try_empty:
                                    action = 'The queue is full.'
                                else:
                                    action = 'The queue is not full.'
                            elif value2 == 6:
                                try_length = queue.getLength()
                                action = "The queue pointer is at: " + str(try_length)

                            #display the action results here
                            #FIRST, GET THE QUEUE CENTERED BASED ON ITS LENGTH
                            print_queue = add_spaces(queue.queue)
                            value2 = screen.show_screen('static', 'queues_result', ['<action>', '<queue>'], [action, print_queue])
                        except:
                            #incorrect action choice is made
                            print_queue = add_spaces(queue.queue)
                            value2 = screen.show_screen('static', 'queues_action_incorrect', ['<queue>'], [print_queue])
                except:
                    #incorrect queue size is given
                    #if bad input is given, respond based on if it was an integer or not.  They might have given a number that was not within
                    #the correct range.  It is better to let them know that then to just say "Incorrect Input" for all cases.
                    if size:
                        value2 = screen.show_screen('static', 'queues_start_incorrect')
                    else:
                        value2 = screen.show_screen('static', 'queues_start_bad_size')



        #OPTION 10, Stack Builder
        elif(value == '10'):
            #This calculates how many spaces should go before the stack in the screen based on the stack's size.
            def add_spaces(the_stack):
                spaces = int((72 - len(str(stack.stack)))/2)
                print_stack = ''
                for x in range(0, spaces):
                    print_stack += ' '
                print_stack += str(stack.stack)
                return print_stack
            error = 0
            value2 = ''

            #main loop
            while(value2.strip().lower() != 'e'):
                size = True
                value2 = screen.show_screen('static', 'stacks_start')
                try:
                    #input testing block
                    stack_size = int(value2)
                    if stack_size < 1 or stack_size > 9:
                        size = False
                        raise Exception()
                    
                    #create stack
                    stack = StackBuilder.stack(stack_size)

                    #action completion loop
                    while(value2.strip().lower() != 'e'):
                        action = ''
                        print_stack = add_spaces(stack.stack)
                        value2 = screen.show_screen('static', 'stacks_action', ['<stack>'], [print_stack])
                        try:
                            #test the input to see if it is an int and if it is in the menu
                            value2 = int(value2)
                            if value2 not in [1, 2, 3, 4, 5, 6]:
                                raise Exception()
                            
                            #action options
                            if value2 == 1:
                                #limit input to 4 characters for stack
                                size_error = False
                                while(True):
                                    if not size_error:
                                        print_stack = add_spaces(stack.stack)
                                        value2 = screen.show_screen('static', 'stacks_action_push', ['<stack>'], [print_stack])
                                    else:
                                        value2 = screen.show_screen('static', 'stacks_action_push_incorrect')
                                    if len(value2) > 4:
                                        pass
                                    else:
                                        break
                                try_push = stack.push(value2)
                                if not try_push:
                                    action = 'Unable to push.  stack full.'
                                else:
                                    action = 'Push completed successfully!'
                            elif value2 == 2:
                                try_pop = stack.pop()
                                if not try_pop:
                                    action = 'Unable to pop.  stack empty.'
                                else:
                                    action = 'Popped ' + str(try_pop) + ' successfully!'
                            elif value2 == 3:
                                try_peek = stack.peek()
                                if not try_peek:
                                    action = 'Unable to peek.  stack is empty.'
                                else:
                                    action = 'The top value is: ' + str(try_peek)
                            elif value2 == 4:
                                try_empty = stack.isEmpty()
                                if try_empty:
                                    action = 'The stack is empty.'
                                else:
                                    action = 'The stack is not empty.'
                            elif value2 == 5:
                                try_empty = stack.isFull()
                                if try_empty:
                                    action = 'The stack is full.'
                                else:
                                    action = 'The stack is not full.'
                            elif value2 == 6:
                                try_length = stack.getPointer()
                                action = "The stack pointer is at: " + str(try_length)

                            #display the action results here
                            #FIRST, GET THE stack CENTERED BASED ON ITS LENGTH
                            print_stack = add_spaces(stack.stack)
                            value2 = screen.show_screen('static', 'stacks_result', ['<action>', '<stack>'], [action, print_stack])
                        except:
                            #incorrect action choice is made
                            print_stack = add_spaces(stack.stack)
                            value2 = screen.show_screen('static', 'stacks_action_incorrect', ['<stack>'], [print_stack])
                except:
                    #incorrect stack size is given
                    #if bad input is given, respond based on if it was an integer or not.  They might have given a number that was not within
                    #the correct range.  It is better to let them know that then to just say "Incorrect Input" for all cases.
                    if size:
                        value2 = screen.show_screen('static', 'stacks_start_incorrect')
                    else:
                        value2 = screen.show_screen('static', 'stacks_start_bad_size')



        #OPTION 11, Stack Sort
        elif(value == '11'):
            error = 0
            value2 = ''
            #main loop
            while(value2.strip().lower() != 'e'):
                input_judge = 0
                value2 = screen.show_screen('static', 'stack_sort_start')
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
                        value2 = screen.show_screen('static', 'stack_sort_start_incorrect')
                    else:
                        display_tags = ['<l1>', '<l2>', '<l3>', '<l4>', '<l5>', '<l6>', '<l7>']
                        data = StackSort.stack_sort(value)
                        data = str(data)
                        display_data = wrap_lines(data, 7, 43)
                        value2 = screen.show_screen('static', 'stack_sort_end', display_tags, display_data)
                else:
                    #if they choose a random list
                    display_tags = ['<l1>', '<l2>', '<l3>', '<l4>', '<l5>', '<l6>', '<l7>']
                    data = StackSort.stack_sort(randomIntList.randomIntList(20, 1, 20))
                    data = str(data)
                    display_data = wrap_lines(data, 7, 43)
                    value2 = screen.show_screen('static', 'stack_sort_end', display_tags, display_data)
                    


        #OPTION 12, About Screen
        elif(value == '12'):
            error = 0
            screen.show_screen('static', 'about')



        #OPTION 12, Exit the Program
        elif(value == '13'):
            break
        else:
            #incorrect input option
            error = 1
    screen.show_screen('static', 'exit')
main()
