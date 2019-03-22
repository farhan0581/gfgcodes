class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, arr):
        max_left = {}
        max_right = {}
        stack = []

        for i, v in enumerate(arr):
            while stack and arr[stack[-1]] <= v:
                stack.pop()
            max_left[i] = stack[-1] if stack else 0
            stack.append(i)

        stack = []
        i = len(arr)-1
        while i >= 0:
            while stack and arr[stack[-1]] <= arr[i]:
                stack.pop()
            max_right[i] = stack[-1] if stack else 0
            stack.append(i)
            i -= 1
        
        i=0
        maxprod = 0
        while i < len(arr)-1:
            prod = ((max_left[i] % 1000000007) * (max_right[i] % 1000000007)) % 1000000007
            if prod > maxprod:
                maxprod = prod
            i += 1
        return maxprod

print(Solution().maxSpecialProduct([  5, 9, 6, 8, 6, 4, 6, 9, 5, 4, 9 ]))

