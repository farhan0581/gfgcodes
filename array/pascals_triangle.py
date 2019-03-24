class Solution:
    # @param A : integer
    # @return a list of list of integers
    # return all the k rows
    def solve(self, n):
        arr = []

        for i in range(n):
            arr.append([None]*(i+1))
            for j in range(i+1):
                if j == 0 or j == i:
                    arr[i][j] = 1
                else:
                    arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        
        return arr
    
    # return a single kth row
    def getRow(self, n):
        n += 1
        arr = []
        prev = [1]

        for i in range(n):
            arr = [None]*(i+1)
            for j in range(i+1):
                if j == 0 or j == i:
                    arr[j] = 1
                else:
                    arr[j] = prev[j-1] + prev[j]
            
            prev = arr[:]
        return arr


# print(Solution().solve(5))
print(Solution().getRow(1))

