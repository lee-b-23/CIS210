#the first piece of data in the returned linked list is always a placeholder
#the last piece of data is not going to point anyhere useful.  I have not found a way to change it.
import LargestNum as lrgn

def orderedLL(array, newLL=[], ignore=[], last=None, maximum=None):    #If it is the first index in the array
    if(last == None):
        print("START")
        r1 = lrgn.largestNum(array, ignore)
        last = r1[0]
        maximum = r1[0]
        newLL = [None] * maximum
        newLL[0] = last
        newLL[last - 1] = last
        ignore.append(r1[1])
        newLL[r1[0] - 1] = r1[1]
        recur = orderedLL(array, newLL, ignore, last, maximum)
    else:
        r1 = lrgn.largestNum(array, ignore)
        print(r1)
        #If the end is reached or an error is encountered.
        if(r1 == False or r1 == None):
            return newLL
        ignore.append(r1[1])         #adds num to ignore list
        newLL[last - 1] = r1[0]
        if(r1[0] == last):
            last = r1[0] - 1
        else:
            last = r1[0]
    recur = orderedLL(array, newLL, ignore, last, maximum)
    return recur

value = orderedLL([1, 2, 3, 6, 5, 4, 9, 7, 8])

print(value)

array1 = []
for x in range(0, len(value)):
    if(value[x] != None):
        array1.append(x)
print(array1)
