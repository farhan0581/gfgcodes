
def getLongestSubarray(nums: [int], k: int) -> int:
    # Write your code here
    maxlen = 0
    start=end=0
    s=nums[0]

    while end < len(nums) and start <= end:
            
        if s <= k:
            if s == k:
                maxlen = max(maxlen, end-start)
            s += nums[end]
            end += 1
        elif s > k:
            s -= nums[start]
            start += 1
            
    if s == k and maxlen == 0:
        return max(end-start, maxlen)
    return maxlen
        



l = [1, 2, 3, 1,0,0,0,0, 1, 1, 1]
l=[-1,1,1]
l=[-1, 0, 1, 1, -1, -1, 0]
k=52
l=[0,2,5,3,3,4,4,3,0,5,5,4,4,4,3,2,0,2,3,1,3,0,4,3,1,4,5,2,4,3,1,4,5,0,3,4,0]
print(getLongestSubarray(l, k))