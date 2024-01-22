class Solution(object):
    result = []
    def findSum(self, arr, target, cursum, nums, i):
        print(nums)
        if i >= len(arr):
            return False
        if target == cursum:
            self.result.append(nums[:])
            return True
        elif cursum > target:
            return False
        
        # move to next number without adding to sum
        self.findSum(arr, target, cursum, nums,i+1)
        
        
        # add sum and start same
        if cursum + arr[i] <= target:
            cursum = cursum + arr[i]
            nums.append(arr[i])
            self.findSum(arr, target, cursum, nums,i)
            # TODO most important
            nums.pop()
        

        # choose sum and move to next
        # below condition is same as first condition 1st call + second condition in 2nd call
        # self.findSum(arr, target, cursum, nums,i+1)
                
        return False




    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.result = []
        self.findSum(candidates, target, 0, [], 0)
        print(self.result)
        


c = [2,3,5]
t = 8
Solution().combinationSum(c,t)