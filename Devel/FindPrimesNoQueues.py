"""
Name:  FindPrimesNoQueues.py
Author:  Lee Brown
Created:  11/02/2020
Last Updated:  11/03/2020
Purpose:  Find all prime numbers given a range or a desired amount.
Description:  This is going to use recursion and lists to find primes.
Sources:
 - https://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists/11520540
Outline:

primes(list, _current_index_ = 0):
    grab current index value
    for every next value:
        check IsFactor(base, potential_factor) for every pair of (next value, _current_index)
        if the answer is a factor:
            change was made
            make that value = none
        else:
            pass
    if change was made:
        increment _current_index_
        Add all items that are not none to the list.
        run a recursive function with teh new list and _current_index_
        return that recursive function result
    else:
        return original list (list)

function2(number_of_primes):
    count = 2
    while I have not found the number of primes that I want
        test = primes_under(count)

        if the length of the test is the length that I want:
            return test
        else:
            count += 1
"""
import IsFactor as fact
class Primes:
    def __init__(self):
        pass
    def _primes_(self, nums, cur = 0):
        #search through and make values equal to None where they need to be.
        change = False
        cur_val = nums[cur]
        for index in range(cur + 1, len(nums)):
            if fact.is_factor(nums[index], cur_val):
                nums[index] = None
                change = True
            else:
                pass
        #remove unwanted values
        c = 0
        while True:
            if c >= len(nums):
                break
            else:
                if nums[c] == None:
                    del nums[c]
                else:
                    c += 1
        #if there was a change made, send that new list back into this function.  Otherwise, return it
        if change:
            cur += 1
            recur = self._primes_(nums, cur)
            return recur
        else:
            return nums
    
    def primes_under(self, maximum):
        #cases that the algorith cannot solve
        if maximum <= 2:
            return []
        elif maximum == 3:
            return [2]
        else:
            pass

        #populate nums
        nums = []
        for x in range(2, maximum):
            nums.append(x)

        result = self._primes_(nums)
        return result

    def n_primes(self, num_of_primes):
        if num_of_primes <= 0:
            return []
        
        count = 3
        while(True):
            test = self.primes_under(count)
            if len(test) == num_of_primes:
                return test
            else:
                count += 1

#example = Primes()
#print(example._primes_([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
#print(example.primes_under(10))
#print(example.n_primes(100))