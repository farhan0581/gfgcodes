'''
A frog is crossing a river. The river is divided into some number of units, and at each unit, there may or may not exist a stone. The frog can jump on a stone, but it must not jump into the water.

Given a list of stones positions (in units) in sorted ascending order, determine if the frog can cross the river by landing on the last stone. Initially, the frog is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 units. The frog can only jump in the forward direction.

 

Example 1:

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th and 6th stone is too large.
 

Constraints:

2 <= stones.length <= 2000
0 <= stones[i] <= 231 - 1
stones[0] == 0
stones is sorted in a strictly increasing order.


APPROACH:
/Users/farhankhan/Desktop/gfgcodes/data/frog_jump.jpg

- We have two variables i and k,
- now based on k, we can go to k, k-1 or k+1 distance
- so we need a map[value] = index,
- ham kisi index pe dekhte hain ki, arr[i]+k, ya arr[i]+k+1 ya arr[i]+k-1 map 
- mein hai ya nahein, agar hai to ham move kar sakte hain, with that new index and value k
'''
class Solution(object):
    def solve(self,arr, m, i, k, dp):
        # print(i,arr[i], k)
        
        if i == len(arr)-1:
            return True
        
        if dp[i][k] != -1:
            return dp[i][k]

        
        n1 = m.get(arr[i]+k, -1)
        n2 = m.get(arr[i]+k+1, -1)
        n3 = m.get(arr[i]+k-1, -1)
        
        p1=p2=p3=False
        
        if n1 != -1 and n1 > i:
            p1 = self.solve(arr, m ,n1, k, dp)
        if n2 != -1 and n2 > i:
            p2 = self.solve(arr, m ,n2, k+1, dp)
        if n3 != -1 and n3 > i:
            p3 = self.solve(arr, m ,n3, k-1, dp)
        
        
        dp[i][k] =  p1 or p2 or p3
        return dp[i][k]
        
        
    def canCross(self, arr):
        """
        :type stones: List[int]
        :rtype: bool
        """
        n = len(arr)
        m = {}
        dp = [[-1 for i in range(2001)] for i in range(n)]
        for i in range(n):
            m[arr[i]] = i
        
        # print(m)
    

        if arr[1] - arr[0] != 1:
            return False
        

        return self.solve(arr,m, 1, 1, dp)


    

l = [0,1,3,5,6,8,12,17]
# l=[0,1,2,3,4,8,9,11]
print(Solution().canCross(l))