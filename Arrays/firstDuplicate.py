# CodeFights

# @param a : numbers in the range from 1 to a.length
# @return the first duplicate number for which the second occurrence has the minimal index. If there are no such elements, return -1

def firstDuplicate(a):

    for i in range(len(a)):
        if( a[abs(a[i])-1] < 0 ):
            return abs(a[i])
        else:
            a[abs(a[i]) - 1] = -a[abs(a[i]) - 1]
    
    return -1
