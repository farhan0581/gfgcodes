'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


APPRoach simple hai
- dono array mila ke hame elements mein se median dena hai



'''
from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        MIN = -9999999999
        MAX = 9999999999
        n1 = len(nums1)
        n2 = len(nums2)

        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        leftportion = (n1+n2+1)//2
        
        left = 0
        right = len(nums1)

        while left <= right:
            mid1 = (left+right)//2
            mid2 = leftportion - mid1
            l1 = l2 = MIN
            r1 = r2 = MAX

            if mid1-1 >= 0:
                l1 = nums1[mid1-1]
            if mid2-1 >= 0:
                l2 = nums2[mid2-1]
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            
            if l1 <= r2 and l2 <= r1:
                if (n1+n2)%2 == 0:
                    return (max(l1, l2) + min(r1, r2))/2
                else:
                    return max(l1, l2)
            elif l1 > r2:
                right = mid1-1
            elif l2 > r1:
                left = mid1+1

            



l1 = [1,3,7,11]
l2 = [2,4,6]
print(Solution().findMedianSortedArrays(l1,l2))