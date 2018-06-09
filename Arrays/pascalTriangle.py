# InterviewBit

# @param A : integer that represents the number of rows of the pascal triangle
# @return a list of list of integers that represents the A rows of the pascal triangle

def generate(self, A):
    if A <= 0:
        return []

    result = [[1]]
 
   for r in range(1, A):
        row = [1]
        for i in range(1,r):
            row.append(result[r-1][i-1] + result[r-1][i])
        row.append(1)
        result.append(row)
    return result
