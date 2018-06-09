# CodeFights

# @param a : n x n 2D matrix that represents an imag
# @return rotated image by 90 degrees (clockwise) in O(1) space complexity

# Solution 1

def rotateImage(a):
    return list(zip(*reversed(a)))

# Solution 2

def rotateImage(a):
    return [[x[i] for x in a][::-1] for i in range(len(a))]

# Solution 3

def rotateImage(a):
    
    for i in range(len(a)/2):
        for j in range(len(a)-1-i*2):
            shift = [ a[len(a)-1-j-i][i], a[i][j+i], a[j+i][len(a)-1-i], a[len(a)-1-i][len(a)-1-j-i] ]
            a[i][j+i] = shift[0]
            a[j+i][len(a)-1-i] = shift[1]
            a[len(a)-1-i][len(a)-1-j-i] = shift[2]
            a[len(a)-1-j-i][i] = shift[3]
    return a
