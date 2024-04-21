'''
You are given a sorted array consisting of only integers where every element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10

APPROACH:
when correct pairs are there then first number of pair will always occur on first position(even)
and second number always occur on second position (odd),
so when there is a mismatch , the sinlge number will be in right half,
otherwise left half

'''
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1

        while start < end:
            mid = (start+end)//2
            if (mid % 2 == 0 and nums[mid] == nums[mid+1]) or (mid % 2 == 1 and nums[mid-1] == nums[mid]):
                start = mid+1
            else:
                end = mid
        
        return nums[start]