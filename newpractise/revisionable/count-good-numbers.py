'''
A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".
Example 2:

Input: n = 4
Output: 400
Example 3:

Input: n = 50
Output: 564908303
'''
class Solution:
    
    # this is the first bruteforce approach
    def solve(self, n, i):
        even = [0,2,4,6,8]
        prime = [2,3,5,7]
        mod = 1e9+7
        if i > n-1:
            return 1
        
        cnt = 0
        
        if i % 2 == 0:
            # for num in even:
            cnt = (cnt + (self.solve(n, i+1)*5)%mod)%mod
        else:
            # for num in prime:
            cnt = (cnt +  (self.solve(n, i+1)*4)%mod)%mod
        
        return int(cnt%mod)
    
    
    def pow(self, num, n):
        mod = int(1e9+7)
        if n == 0:
            return 1
        
        # return (num*(self.pow(num, n-1))%mod)%mod

        if n % 2 == 0:
            # return self.pow(num, n//2)*self.pow(num, n//2) this was correct but giving TLE
            # the trick here is to avoid function calls for tle
            return self.pow(num*num%mod, n//2)%mod
        else:
            return (self.pow(num*num%mod, n//2)*num)%mod

        

    def countGoodNumbers(self, n: int) -> int:
        mod = int(1e9+7)
        p1 = 0
        p2 = 0

        if n % 2 == 0:
            p1 = n // 2
        else:
            p1 = n//2 + 1
        p2 = n//2
        
        res = (self.pow(5, p1)%mod * self.pow(4, p2)%mod)%mod
        return res

        