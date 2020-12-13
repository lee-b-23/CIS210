"""
This program's purpose is to find all of the numbers in an array which have three as a factor.

Author: Lee Brown
Name: threeFactors.py
Date:  9/12/2020
Last Updated:  12/08/2020
"""
from . import randomIntList as r
from . import timer


def addPlaces(num):
    result = 0
    for x in range(0, len(str(num))):
        if(str(num)[x] != "-"):                           #if num is negative
            result = result + int(str(num)[x])
        else:
            pass
    return(result)

def threeFactors(array):
    resultsArray = []
    factorsCounter = 0
    for x in range(0, len(array)):
        total = addPlaces(array[x])
        while(len(str(total)) > 1):
            total = addPlaces(total)

        if(total == 3 or total == 6 or total == 9):
            resultsArray.append(array[x])
            factorsCounter = factorsCounter + 1
        else:
            pass
    return(resultsArray)

if __name__ == '__main__':
    array = r.randomIntList(1000, -5000, 5000)
    #print(array)
    print("")
    totalFactors = threeFactors(array)
    print("---factors of three---")
    print(len(totalFactors))
    print(totalFactors)
