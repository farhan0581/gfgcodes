'''
Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

 

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Approach:
- we have to use similar approach like merge sort but there is a catch



'''
from typing import List

class Solution:
    
    def merge(self, arr, start, end, mid, ans):

        tmp = []
        i = start
        j = mid+1

        cnt = 0

        while i <= mid and j <= end:
            if arr[i][0] <= arr[j][0]:
                tmp.append((arr[i][0], arr[i][1]))
                ans[arr[i][1]] += cnt
                i += 1
            else:
                tmp.append((arr[j][0], arr[j][1]))
                cnt += 1

                # this was giving TLE
                # for k in range(i, mid+1):
                #     ans[arr[k][1]] += 1

                j += 1
        
        while i <= mid:
            tmp.append((arr[i][0], arr[i][1]))
            ans[arr[i][1]] += cnt
            i += 1
        
        while j <= end:
            tmp.append((arr[j][0], arr[j][1]))
            j += 1
        
        for i in range(len(tmp)):
            arr[start+i] = tmp[i]
        
        return ans
        
    
    def mergesort(self, arr, start, end, ans):
        if start >= end:
            return ans
        mid = (start+end)//2

        ans = self.mergesort(arr, start, mid, ans)
        ans = self.mergesort(arr, mid+1, end, ans)

        return self.merge(arr, start, end, mid, ans)

    
    def countSmaller(self, nums: List[int]) -> List[int]:
        nums = [(y,x) for x,y in enumerate(nums)]
        ans = [0 for i in range(len(nums))]
        self.mergesort(nums, 0, len(nums)-1, ans)
        
        # print(nums)
        return ans

l = [5,2,6,1]
l = [-1, -1]
print(Solution().countSmaller(l))
# print(l)