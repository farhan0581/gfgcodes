import operator

class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, arr):
        operators = ['+', '-', '*', '/']
        stack = []
        allowed_operators = {
                                "+": operator.add,
                                "-": operator.sub,
                                "*": operator.mul,
                                "/": operator.floordiv
                            }
        for elem in arr:
            if elem not in operators:
                stack.append(int(elem))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                res = allowed_operators[elem](op1, op2)
                stack.append(res)
        return stack[0]

print(Solution().evalRPN(["4", "13", "5", "/", "+"]))
