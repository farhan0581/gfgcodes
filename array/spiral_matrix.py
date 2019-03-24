class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generateMatrix(self, n):
        count = 1

        cstart = 0
        cend = n

        arr = [[None for m in xrange(n)] for _n in xrange(n)]
        # print(arr)
        while count <= n*n:
            # print(arr)
            i = cstart
            for j in xrange(cstart, cend):
                # print(i,j)
                arr[i][j] = count
                count += 1
            
            for i in xrange(cstart+1, cend):
                # print(i,j)
                
                arr[i][j] = count
                count += 1

            j = cend-2
            while j >= cstart:
                # print(i,j)
                arr[i][j] = count
                count += 1
                j -= 1

            j += 1
            i = cend-2
            while i > cstart:
                # print(i,j)
                arr[i][j] = count
                count+= 1
                i -= 1

            cstart += 1
            cend -= 1
        
        return arr


print(Solution().generateMatrix(1))
