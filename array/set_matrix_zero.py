class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, arr):
        r, c, rr, cc, z = len(arr), len(arr[0]), 1, 1, 1
        for i in xrange(r):
            for j in xrange(c):
                if arr[i][j] != 0:
                    continue
                arr[i][0] = 2
                arr[0][j] = 2

                if i == 0:
                    rr = 0
                if j == 0:
                    cc = 0
                if i == 0 and j == 0:
                    z = 0
        # print(arr, z, rr, cc)
        for i in xrange(1, r):
            if arr[i][0] != 2:
                continue
            for j in xrange(0, c):
                arr[i][j] = 0
        # print(arr)
        for i in xrange(1, c):
            # print("sakjfdhdsakfhkj", arr[0][])
            if arr[0][i] != 2:
                continue
            # print(0, i)
            for j in xrange(0, r):
                arr[j][i] = 0
        if z == 0 or (rr ==0 and cc == 0):
            for i in xrange(r):
                arr[i][0] = 0
            for i in xrange(c):
                arr[0][i] = 0
        elif rr == 0:
            for i in xrange(c):
                arr[0][i] = 0
        elif cc == 0:
            for i in xrange(r):
                arr[i][0] = 0
            
        return arr
print(Solution().setZeroes([[1,0,1],[1,1,1],[1,1,1]]))
print(Solution().setZeroes([[0,0],[1,1]]))
