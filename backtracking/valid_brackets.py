class Solution:
    # @param A : integer
    # @return a list of strings

    def _solve(self, string, left, right, index, n):

        if right == n:
            self.res.append(''.join(string))
            return
        
        else:
            if left < n:
                string[index] = '('
                self._solve(string, left+1, right, index+1, n)

            if left > right:
                string[index]  = ')'
                self._solve(string, left, right+1, index+1, n)
        



    def generateParenthesis(self, n):
        self.res = []
        string = [''] * 2 * n
        self._solve(string, 0, 0, 0, n)
        return self.res

print(Solution().generateParenthesis(3))
