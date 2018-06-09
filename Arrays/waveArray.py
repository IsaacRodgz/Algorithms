# InterviewBit

# @param A : list of integers
# @return a sortet array into a wave like array. Arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....

def wave(self, A):
    if len(A) == 0 or len(A) == 1:
        return A
        
    A.sort()
    for i in range(0, len(A)-1, 2):
        temp = A[i]
        A[i] = A[i+1]
        A[i+1] = temp
        
    return A
