class Solution:
    # @param A : list of integers
    # @return an integer

    def cntones(self, num):
        count = 0
        # x=num
        # while num:
            # if num &1:
                # count += 1
            # num = num >> 1
        return bin(num).count('1')

    def cntBits(self, lis):
        modulo = 1000000007
        result = 0
        i = 0
        length = len(lis)
        for i in range(length):
            j = i + 1
            while j < length:
                res = lis[i]^lis[j]
                j += 1
                result += (self.cntones(res))%modulo
        return (result*2) % modulo

print(Solution().cntBits([81, 13, 2, 7, 96]))