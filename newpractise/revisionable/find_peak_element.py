'''
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

--------------------------------------
MOST IMPORTANT CONSTRAINT IS:
nums[i] != nums[i + 1] for all valid i.
--------------------------------------

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index number 1 where the peak element is 2, or index number 5 where the peak element is 6.


APPROACH:
There are 3 cases:
- case1 : mid is peak, that is mid is greater than its neighbours
- case2: mid is smaller than left neighbour -> go left
- case3 : mid is smaller than its right neighbour -> go right

'''


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        start = 1
        end = len(nums)-2

        if len(nums) == 1:
            return 0
        
        if nums[0] > nums[1]:
            return 0
        
        if nums[-1] > nums[-2]:
            return len(nums)-1

        while start <= end:
            mid = (start+end)//2

            if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                return mid
            
            elif nums[b co[rpfl;vc ;çscx]] < nums[mid-1]:
                end = mid-1
            
            elif nums[mid] < nums[mid+1]:
                start = mid+1
        
        return -1


        