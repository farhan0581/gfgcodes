class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, xarr, yarr):
        steps = 0
        for i in xrange(len(xarr)):
            if i+1 < len(xarr):
                dist_x = abs(xarr[i+1]-xarr[i])
                dist_y = abs(yarr[i+1]-yarr[i])
                steps += max(dist_x, dist_y)
        return steps

print(Solution().coverPoints( [-2],[7]))