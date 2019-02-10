class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, abs_path):
        stack = []
        path = abs_path.split("/")
        for elem in path:
            if elem == '..':
                try:
                    stack.pop()
                except:
                    pass
            elif elem == '.':
                pass
            elif elem.strip() != '':
                stack.append(elem)
        result = "/%s" % ('/'.join(stack))
        return result
        

print(Solution().simplifyPath("/../"))