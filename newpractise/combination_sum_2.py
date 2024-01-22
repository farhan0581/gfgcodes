class Solution(object):

    result = []
    def findSum(self, arr, target, cursum, nums, i):
        if cursum == target:
            self.result.append(nums[:])
            return
        elif cursum > target:
            return
        if i >= len(arr):
            return
        
        # choose sum
        if cursum + arr[i] <= target:
            nums.append(arr[i])
            # cursum += arr[i] this is wrong, we cannot update cursum
            self.findSum(arr, target, cursum+arr[i], nums, i+1)
            nums.pop()


        # what we are doing is basically skipping if the element we choose above , does not carry over
        # to the next step in the recursion, otherwsie we will get duplicate results also
        # so by doing this we do not send the same element to be choosen again in the recursion tree.
        # dont worry the repeated elements will be taken care in the above recursion call
        j = i+1

        while j < len(arr) and arr[i] == arr[j]:
            j += 1
            continue

        # not choose sum
        self.findSum(arr, target, cursum, nums, j)

 
        return
            


    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """

        self.result = []
        candidates = sorted(candidates)
        self.findSum(candidates, target, 0, [], 0)
        return self.result

        

c =[10,1,2,7,6,1,5]
# c = [2,5,2,1,2]
target = 8
# target = 5
print(Solution().combinationSum2(c,target))