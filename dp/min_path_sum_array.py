class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, arr):
        import sys
        MAX = sys.maxsize

        for i in xrange(len(arr)):
            for j in xrange(len(arr[i])):

                if i-1 < 0:
                    up = MAX
                else:
                    up = arr[i-1][j]
                if j-1 < 0:
                    right = MAX
                else:
                    right = arr[i][j-1]
                
                if up == MAX and right == MAX:
                    up = right = 0
                
                cost = arr[i][j] + min(up, right)

                arr[i][j] = cost
        return arr[i][j]

a = [  [1, 3, 2],
       [4, 3, 1],
       [5, 6, 1]
    ]
print(Solution().minPathSum(a))


