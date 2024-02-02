'''
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

'''
class Solution(object):
    def _longestOnes(self, A, K):
      left = right = 0
      
      for right in range(len(A)):
        # if we encounter a 0 the we decrement K
        if A[right] == 0:
          K -= 1
        # else no impact to K
        
        # if K < 0 then we need to move the left part of the window forward
        # to try and remove the extra 0's
        if K < 0:
          # if the left one was zero then we adjust K
          if A[left] == 0:
            K += 1
          # regardless of whether we had a 1 or a 0 we can move left side by 1
          # if we keep seeing 1's the window still keeps moving as-is
          left += 1
      
      return right - left + 1
    
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        max1 = 0
        start = 0
        end = 0

        while end < len(nums):
            print(start,end,k)
            
            if k >= 0:
                if nums[end] == 0:
                    k -= 1
                end += 1
            
            # ye else nahein hogi, isi liye nahein chal raha tha
            if k < 0:
                if nums[start] == 0:
                    k += 1
                
                start += 1
           
            max1 = max(max1, (end-start))

        return max1

        
# l =[1,1,1,0,0,0,1,1,1,1,0]
l=[0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# l = [1,1,1,0,0,1,0,0]
# l = [0,0,1,0]
k = 2
print(Solution().longestOnes(l,k))