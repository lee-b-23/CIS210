def largestNum(array, ignore):
    #print("Called")
    '''print(len(ignore))
    print(len(array))
    print("")'''
    if(len(ignore) == len(array)):
        print("exited")
        return False
    if not array:
        print("ERROR:  Array is empty.")
        return None
    
    for i in range(0, len(array)):
        if i in ignore:
            pass
        else:
            temp = array[i]
    c = 0
    for x in array:
        if (x >= temp and c not in ignore):
            temp = x
            index = c
        c = c + 1
    return [temp,index]
