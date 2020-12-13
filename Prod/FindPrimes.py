"""
Name:  FindPrimes.py
Author:  Lee Brown
Created:  10/27/2020
Last Updated:  11/01/2020
Purpose:  This will find all prime numbers below a given number.
Description:  This is going to use queues and recursion to find all prime numbers
            below a given number.
Helpful Sources:
 - https://dbader.org/blog/meaning-of-underscores-in-python#:~:text=The%20underscore%20prefix%20is%20meant,public%E2%80%9D%20variables%20like%20Java%20does.
IDEAS:
 - Use stacks to sort??????????????????
"""
import Queues
import IsFactor as fact
import StackBuilder as stack
import StackSort as sort
import time

def find_primes(maximum, _primes_ = None, _changes_ = 0, _recursions_ = 0):
    #if on the first call, there will be no recursion
    if _primes_ == None:
        pass
    else:
        _recursions_ = _recursions_ + 1

    #If the max is 2 or 3, the algorithm following this section will not work.
    if(maximum == 2):
        result = Queues.Queue(1)
        result.enqueue(2)
        return result.queue
    elif(maximum == 3):
        result = [2, 3]
        return result
    

    #create return queue
    _queue2_ = Queues.Queue(maximum - _changes_ - 1)
    
    #if this is the first call in the recursion cycle, populate the queue
    if _primes_ == None:
        _primes_ = Queues.Queue(maximum - 1)
        for x in range(2, maximum + 1):
            _primes_.enqueue(x)

    #grab the first item from the queue
    first_item = _primes_.dequeue()
    done = True

    
    #the primary loop
    while(True):
        next_item = _primes_.dequeue()
        if fact.is_factor(next_item, first_item) == True:
            done = False
            _changes_ = _changes_ + 1
        else:
            _queue2_.enqueue(next_item)

        if(_primes_.isEmpty() == True):
            break
        else:
            pass
    #if a change was made above
    if(done == False):
        value = find_primes(maximum, _queue2_, _changes_, _recursions_)
        value.enqueue(first_item)
        if _recursions_ == 0:
            result = sort.stack_sort(value.queue)
            return result
        else:
            return value
    else:
        if _recursions_ == 0:
            result = sort.stack_sort(_queue2_.queue)
            return result
        else:
            _queue2_.enqueue(first_item)
            unsorted = _queue2_
            return unsorted

def return_x_primes(num):
    x = 2
    while True:
        test = find_primes(x)
        if len(test) == num:
            time.sleep(5)
            break
        else:
            x += 1
    return test

if __name__ == '__main__':
    
    value = return_x_primes(100)
    print(value)
    print("Length of list = " + str(len(value)))

#print(find_primes(1000))
