'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 

Example 1:
https://assets.leetcode.com/uploads/2018/10/22/rainwatertrap.png
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.


APPROACH:
the trick is to use the left max and right max and store it
time:O(3N) space:O(2N) => not optimized
'''
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0]*len(height)
        right_max = [0]*len(height)

        left = 0
        
        for i in range(len(height)):
            left = max(left, height[i])
            left_max[i] = left
        
        i = len(height)-1
        right = 0
        while i >= 0:
            right = max(right, height[i])
            right_max[i] = right
            i -= 1
        
        water = 0
        for i in range(len(height)):
            water += min(left_max[i], right_max[i]) - height[i]
        return water
        
        