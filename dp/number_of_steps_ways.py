# https://www.geeksforgeeks.org/count-ways-reach-nth-stair/
class Solution:
    # @param A : integer
    # @return an integer
    
    def traverse(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        try:
            s1 = self.map[n-1]
        except KeyError:
            s1 = self.traverse(n-1)
            self.map[n-1] = s1
        try:
            s2 = self.map[n-2]
        except KeyError:            
            s2 = self.traverse(n-2)
            self.map[n-2] = s2

        return s1+s2
        

    def climbStairs(self, n):
        self.map = {}
        steps = self.traverse(n)
        return steps


print(Solution().climbStairs(36))