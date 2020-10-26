import LargestNum as l
import randomIntList as r
import timer

def orderedLL(array, newLL = [], ignore=[]):
    num = l.largestNum(array, ignore)
    if(num == False):
        return newLL
    else:
        newLL.append(num[1])
        ignore.append(num[1])
    value = orderedLL(array, newLL, ignore)
    return value

t = timer.timer()
t.startTimer()
array = r.randomIntList(1000, -100, 100)
value = orderedLL(array)
print(t.endTimer())
print(array)
print(value)
