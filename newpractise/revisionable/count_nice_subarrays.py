''''
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There is no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
'''
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        cnt = 0
        s = 0
        m = {}

        for i in range(len(nums)):
            if nums[i] % 2!= 0:
                s += 1
            
            if s == k:
                cnt += 1
            
            rsum = s-k
            pos = m.get(rsum, -1)
            if pos != -1:
                cnt += len(pos)
            
            try:
                tmp = m[s]
                tmp.append(i)
                m[s] = tmp
            except:
                m[s] = [i]
        
        return cnt
