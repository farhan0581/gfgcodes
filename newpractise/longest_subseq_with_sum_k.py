
# here the prefix sum is optimal method
def getLongestSubarray(nums: [int], k: int) -> int:
    # Write your code here
    maxlen = 0
    start=end=s=0
    m = {}

    while end < len(nums):
        s += nums[end]
        if s == k:
            maxlen = max(maxlen, end+1)
        

        presum = m.get(s-k, -1)
        if presum != -1:
            maxlen = max(maxlen, end-presum)


        try:
            m[s]
        except:
            m[s] = end
        end += 1

        
    return maxlen
        



l = [1, 2, 3, 1,0,0,0,0, 1, 1, 1]
l=[-1,1,1]
l=[-1, 0, 1, 1, -1, -1, 0]
k=52
l=[0,2,5,3,3,4,4,3,0,5,5,4,4,4,3,2,0,2,3,1,3,0,4,3,1,4,5,2,4,3,1,4,5,0,3,4,0]
# print(getLongestSubarray(l, k))



max = 90
n = 29
a = ord('A') + n
if a > max:
    a = a-26
print(a)
# print(ord('Z'))
print(chr(a))