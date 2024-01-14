class Solution:
    # @param A : list of integers
    # @return an integer
    def bulbs(self, arr):
        flips = 0

        for i in xrange(len(arr)):
            if flips % 2 == 0:
                if arr[i] == 0:
                    flips += 1
            else:
                if arr[i] == 1:
                    flips += 1
        
        return flips

# print(Solution().bulbs([0,1,0,1]))
print(Solution().bulbs([1,0,0,0,0]))
