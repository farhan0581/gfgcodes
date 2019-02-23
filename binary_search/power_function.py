class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    def pow(self, num, exp, d):
        #base
        if exp == 1:
            return num%d
        elif exp == 0:
            return 1%d

        # compute this only once
        p = self.pow(num,exp/2,d)

        if exp%2 == 0:
            return (p*p)%d
        else:
            return (p*p*num)%d

print(Solution().pow(71045970,41535484,64735492))