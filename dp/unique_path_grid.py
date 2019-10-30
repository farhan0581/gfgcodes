class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, arr):
        import sys
        MAX = sys.maxsize
        cost = [[0 for x in xrange(len(arr[0]))] for x in xrange(len(arr))]
        if arr[0][0] == 1:
            return 0
        else:
            cost[0][0] = 1

        for i in xrange(len(arr)):
            for j in xrange(len(arr[i])):
                print(cost)
                if arr[i][j] == 1:
                    cost[i][j] = 0
                else:
                    s = 0
                    if i-1 >= 0:
                        s += cost[i-1][j]
                    if j-1 >= 0:
                        s += cost[i][j-1]
                    print(s)
                    if i==0 and j==0:
                        pass
                    else:
                        print('===========')
                        cost[i][j] = s
        print(cost)
        return cost[i][j]

a = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print(Solution().uniquePathsWithObstacles(a))
                
