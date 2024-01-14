'''
Given an array nums of n integers, return an array of all the unique quadruplets
[nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.


using 2 pointer approach in the inner loop and fix variables i and j
similarly in 3 sum we will fix 1 variable.
so order os nlogn + n2

but did not understand logic for line 33 and 34

'''


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        nums = [i for i in sorted(enumerate(nums), key=lambda x:x[1])]
        m = {}
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                k = j + 1
                l = len(nums)-1
                while k < l:    
                    if nums[i][1]+nums[j][1]+nums[k][1]+nums[l][1] == target:
                        key = "%d_%d_%d_%d" % (nums[i][1],nums[j][1],nums[k][1],nums[l][1])
                        try:
                            v = m[key]
                        except:
                            m[key] = 1
                            result.append([nums[i][1],nums[j][1],nums[k][1],nums[l][1]])
                        k += 1
                        l -= 1
                    elif nums[i][1]+nums[j][1]+nums[k][1]+nums[l][1] > target:
                        l -= 1                    
                    elif nums[i][1]+nums[j][1]+nums[k][1]+nums[l][1] < target:
                        k += 1
        return result

