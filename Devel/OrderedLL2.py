import LargestNum as l

def orderedLL(array, newLL = [], ignore=[]):
    num = l.largestNum(array, ignore)
    if(num == False):
        return newLL
    else:
        newLL.append(num[1])
        ignore.append(num[1])
    value = orderedLL(array, newLL, ignore)
    return value

array = [-1, 3, 2, -5, 3, 100]
value = orderedLL(array)
print(array)
print(value)
