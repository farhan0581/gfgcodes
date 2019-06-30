class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, mice, hole):
        mice = sorted(mice)
        hole = sorted(hole)

        m = -999999999999

        for i in xrange(len(mice)):
            diff = abs(mice[i]-hole[i])
            if diff > m:
                m = diff
        return m

print(Solution().mice([4, -4, 2],[4,0,5]))