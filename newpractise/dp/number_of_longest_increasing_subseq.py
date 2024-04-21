'''
count is intereseting
'''

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1]*n
        cnt = [1]*n
        maxi = 1
        ind = 0

        for i in range(n):
            for prev in range(i):
                # this is first time you see the grater value, so just copy the prev
                if nums[i] > nums[prev] and dp[i] < 1+dp[prev]:
                    dp[i] = 1+dp[prev]
                    cnt[i] = cnt[prev]
                # this is repeat, now add this value
                elif nums[i] > nums[prev] and dp[i] == 1+dp[prev]:
                    cnt[i] += cnt[prev]
                
                maxi = max(dp[i], maxi)
        
        maxcnt = 0
        # print(dp, cnt)
        for i in range(n):
            if dp[i] == maxi:
                maxcnt += cnt[i]
        
        return maxcnt