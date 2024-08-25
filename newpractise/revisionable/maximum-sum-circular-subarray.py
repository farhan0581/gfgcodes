'''
Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

Example 1:

Input: nums = [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3.
Example 2:

Input: nums = [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10.
Example 3:

Input: nums = [-3,-2,-3]
Output: -2
Explanation: Subarray [-2] has maximum sum -2.


APPROACH
1. we can apply kadane to find the maxsum subarray
2. but since the array is circular, there is a catch

|----prefix1----|-------s2--------|---prefix2----|

<-----------------full array------------------->

now prefix1+prefix2 can also be a valid candidate,
in this case , normal kadane will fail

let s1 = prefix1+prefix2
s2 is remaining sum then, we have

s1+s2 = sum(array)

now s2 will be minimum subarray in order to s1 become max, proof by contradiction
so we need to just find minimum sum subarray and subtract from sum to get circular wala case,
thats it!!!

'''
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:

        maxsum = nums[0]
        minsum = nums[0]

        s = nums[0]
        s2 = nums[0]

        for i in range(1, len(nums)):
            s = max(s+nums[i], nums[i])
            s2 = min(s2+nums[i], nums[i])
            
            maxsum = max(maxsum, s)
            minsum = min(minsum, s2)

        

        if maxsum > 0:
            return max(maxsum, sum(nums)-minsum)
        
        # this means the entire array is negative, so corner prefix sum will not exist
        return maxsum