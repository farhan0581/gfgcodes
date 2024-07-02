'''
Problem Statement: Given an array of integers that may contain duplicates the task is to return all possible subsets. Return only unique subsets and they can be in any order.

Examples:

Example 1:

Input: array[] = [1,2,2]

Output: [ [ ],[1],[1,2],[1,2,2],[2],[2,2] ]

Explanation: We can have subsets ranging from  length 0 to 3. which are listed above. Also the subset [1,2] appears twice but is printed only once as we require only unique subsets.

Input: array[] = [1]

Output: [ [ ], [1] ]

Explanation: Only two unique subsets are available
'''

class Solution(object):
    r = []
    m = {}
    def recur(self, arr, i, nums):
        if i >= len(nums):
            k = '_'.join(map(str, sorted(arr)))
            try:
                self.m[k]
            except:
                self.m[k] = 1
                self.r.append([i for i in arr])
            return

        # we have 2 choices:
        # we select and we discard
        # here we take the element
        arr.append(nums[i])
        self.recur(arr, i+1, nums)
        
        # here we exclude the element
        arr.pop()
        self.recur(arr, i+1, nums)
        

    # /Users/farhankhan/Desktop/gfgcodes/data/print-all-subsets.png
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = [4,4,4,1,4]

        self.recur([], 0, nums)
        print(self.r)

Solution().subsetsWithDup([])
