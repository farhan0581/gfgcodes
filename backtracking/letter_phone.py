class Solution:

    def printword(self, words, cur_index, result, n, r):
        if cur_index == n:
            _r = ''.join(result)
            r.append(_r)
            return r
        
        for char in self.m[words[cur_index]]:
            result[cur_index] = char
            r = self.printword(words, cur_index+1, result, n, r)

        return r
    
    def letterCombinations(self, arr):
        r = []
        self.m = {
            '0': '0',
            '1': '1',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        res = [None]*len(arr)

        r = self.printword(arr, 0, res, len(arr), r)
        return r
    
print(Solution().letterCombinations("02"))