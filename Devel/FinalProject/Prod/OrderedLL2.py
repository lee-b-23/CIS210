from . import LargestNum as l
from . import randomIntList as r
from . import timer

def orderedLL(array, newLL = [], ignore=[]):
    num = l.largestNum(array, ignore)
    if(num == False):
        return newLL
    else:
        newLL.append(num[1])
        ignore.append(num[1])
    value = orderedLL(array, newLL, ignore)
    return value
'''
t = timer.timer()
t.startTimer()
array = r.randomIntList(10, -100, 100)
value = orderedLL(array)
print(t.endTimer())
print(array)
print(value)
'''
