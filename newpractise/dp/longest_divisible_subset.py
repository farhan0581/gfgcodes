from typing import List

def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dp = [1]*len(nums)
        ans = []
        m = {}
        maxi = 0
        ind = 0


        for i in range(len(nums)):
            m[i] = i
            for prev in range(i):
                if nums[i] % nums[prev] == 0:
                    if 1+dp[prev] > dp[i]:
                        dp[i] = 1+dp[prev]
                        m[i] = prev
                    # dp[i] = max(dp[i], 1+dp[prev])
                
            if dp[i] > maxi:
                maxi = dp[i]
                ind = i

        # print(m, maxi, ind, dp)
        while True:
            ans.append(nums[ind])
            prev = m[ind]
            if prev != ind:
                ind = prev
            else:
                break
        
        return ans[::-1]