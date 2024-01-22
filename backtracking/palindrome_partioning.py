class Solution:
    # @param A : string
    # @return a list of list of strings
    
    def check_palindrome(self, arr):
        start = 0
        end = len(arr)-1
        while start <=end:
            if arr[start] != arr[end]:
                return False
            start += 1
            end -= 1
        # print(arr)
        return True


    # generating all possible susstrings, bruteforce solution and then checking
    def solve(self, arr, res):
        end = 1
        while end <= len(arr):
            for start in range(len(arr)):
                if start+end <= len(arr):
                    _s = arr[start:start+end]
                    if self.check_palindrome(_s):
                        # left = self._solve(arr[0:start], res)
                        if start+end < len(arr):
                            right = self._solve(arr[start+end+1:], res)
                        else:
                            right = True
                        if right:
                            print(_s)
                            print(start, end)

            end += 1
    

    def _solve(self, arr, res, substr, start):

        if start >= len(arr):
            res.append(substr[:])

        
        for i in range(start, len(arr)):
            if self.check_palindrome(arr[start:i+1]):
                substr.append(''.join(arr[start:i+1]))
                self._solve(arr, res, substr, i+1)
                substr.pop()
        

    def partition(self, string):
        arr = list(string)
        res = []
        self._solve(arr, res, [], 0)
        return res
        # print(self.check_palindrome(''))

print(Solution().partition('aab'))
        

