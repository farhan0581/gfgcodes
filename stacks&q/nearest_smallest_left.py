class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, arr):
        stack = []
        result = []
        for elem in arr:
            try:
                while stack[-1] >= elem:
                    stack.pop()
                result.append(stack[-1])
            except:
                result.append(-1)
            stack.append(elem)
        return result

print(Solution().prevSmaller([1,2,3,4,5]))
