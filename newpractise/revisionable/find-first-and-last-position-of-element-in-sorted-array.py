'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

ALSO SAME THING FOR UPPER AND LOWER BOUND

'''
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        r1 = -1
        r2 = -1

        start = 0
        end = len(nums)-1

        # lower bound
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                r1 = mid
                end = mid-1
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid+1
        
        
        if r1 == -1:
            return [-1, -1]


        start = 0
        end = len(nums)-1

        # upper bound
        while start <= end:
            mid = (start+end)//2
            if nums[mid] == target:
                r2 = mid
                start = mid+1
            elif nums[mid] > target:
                end = mid-1
            else:
                start = mid+1


        return [r1,r2]
            
