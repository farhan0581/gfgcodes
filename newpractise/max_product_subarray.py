'''
Given an integer array nums, find a 
subarray
 that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

 

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        leftmax = [None for i in range(len(nums))]  
        rightmax = [None for i in range(len(nums))]  

        j = len(nums)-1
        previ = 1
        prevj = 1
        INT_MIN = -9999999999
        ans = INT_MIN

        for i in range(len(nums)):
            if nums[i] == 0:
                leftmax[i] = INT_MIN
                previ = 1
                ans = 0
            else:
                leftmax[i] = nums[i]*previ
                previ = leftmax[i]
                
            
            if nums[j] == 0:
                rightmax[j] = INT_MIN
                prevj = 1
            else:
                rightmax[j] = nums[j]*prevj
                prevj = rightmax[j]

            ans=max(ans, leftmax[i], rightmax[j]) 

            j -= 1
        # print(leftmax, rightmax)
        # ans = INT_MIN
        # for i in range(len(nums)):
        #     ans=max(ans, leftmax[i], rightmax[i]) 
        return ans

            



    