# InterviewBit

# @param A : Array of integers
# @return an integer. Find the contiguous subarray within an array (containing at least one number) which has the largest sum

def maxSubArray(self, A):
    sum_current = A[0]
    sum_max = A[0]
        
    for i in range(1, len(A)):
        sum_current = max(A[i], A[i]+sum_current)
        sum_max = max(sum_current, sum_max)
       
    return sum_max
