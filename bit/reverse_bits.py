class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, num):
        bits = 32

        rev = 0
        count = 0
        while num > 0:
            rev = rev << 1
            if num&1 == 1:
                rev = rev^1
            num = num>>1
            count += 1
        while count < bits:
            rev = rev << 1
            count += 1
        return rev

print(Solution().reverse(3))
        
        

