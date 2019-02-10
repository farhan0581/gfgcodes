class Solution:
    # @param A : string
    # @return an integer
    def braces(self, exp):
        stack = []
        i = 0
        while i < len(exp):
            char = exp[i]
            if char == ')':
                count = 0
                elem = stack.pop()
                while elem != '(':
                    count += 1
                    elem = stack.pop()
                if count <= 1:
                    return 1         
            else:
                stack.append(char)
            i += 1
        return 0

print(Solution().braces("(a+(a+b))"))