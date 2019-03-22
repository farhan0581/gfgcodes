class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, arr):
        sum = 0
        maxsum = -99999999999
        
        for i in xrange(len(arr)):
            
            sum += arr[i]
            if sum >= maxsum:
                # print(sum,i)
                maxsum = sum
            if sum < 0:
                sum=0

        return maxsum





print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
print(Solution().maxSubArray([-10,-9]))