class Solution:
    # @param A : integer
    # @return an integer
    def _numSetBits(self, num):
        count = 0
        while num > 0:
            count += num % 2
            num /= 2
        return count
    
    def numSetBits(self, num):
        count = 0
        while num > 0:
            count += num & 1
            num = num >> 1
        return count

print(Solution().numSetBits(15))
            

