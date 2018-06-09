# InterviewBit
    
# @param A : non-negative number represented as an array of digits
# @return a list of integers. Add 1 to the number ( increment the number represented by the digits )

def plusOne(self, A):
    val = 1
    for i in range(len(A), 0, -1):
        val = val + A[i-1]
        borrow = int(val/10)
        
        if borrow == 0:
            A[i-1] = val
            break;
        else:
            A[i-1] = val%10
            val = borrow
            
    A = [borrow] + A
    
    while A[0] == 0:
        del A[0]
    return A
