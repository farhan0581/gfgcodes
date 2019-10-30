class Solution:
    # @param A : integer
    # @return a list of integers

    def _solve(self, res, num, n):
        if n == 0:
            print(num)
            res.append(num)
            return

        self._solve(res, num, n-1)
        num = num ^ (1 << (n-1))
        self._solve(res, num, n-1)

    def grayCode(self, n):
        res = []
        num = 0
        self._solve(res, num, n)
        return res

print(Solution().grayCode(3))