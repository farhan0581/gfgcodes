'''
Given an array having both positive and negative integers. The task is to compute the length 
of the largest subarray with sum 0.

Example 1:

Input:
N = 8
A[] = {15,-2,2,-8,1,7,10,23}
Output: 5
Explanation: The largest subarray with
sum 0 will be -2 2 -8 1 7.


Approach:
agar sum(i,j) = S 
and sum(i,x) = S
is ka matlab sum(x+1,j) = 0 raha hoga jabhi ye possible hai
bas yaheeh use karna hai, 
map mein pehla index store karna hai, because repeat bhi hua sum phir bhi hamein pehla wala
hi rakhna hai
so that the range is max

map[prefix_sum] = pahla_index_jahan_mila


Bas ek cheez aur

agar prefix sum kabhi zero mile to hamein wo wali condition bhi dekhna hai



'''


class Solution:
    def maxLen(self, n, arr):
        #Code here
        m = {}
        maxlen = 0
        s = 0

        for i in range(n):
            # print(m)
            s += arr[i]

            if s == 0:
                maxlen = max(maxlen, i+1)

            ind = m.get(s, -1)
            if ind == -1:
                m[s] = i
            else:
                maxlen = max(maxlen, (i-ind))
        return maxlen
                
                






l=[-1,1,-1,1]
# l=[15,-2,2,-8,1,7,10,23]
n = len(l)
# l = [6,-2,2,-8,1,7,4,-10]
print(Solution().maxLen(n,l))