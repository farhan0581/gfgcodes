class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, root, k):
        stack = []
        next = root
        count = 0
        while True:
            if next:
                stack.append(next)
                next = next.left
            else:
                if len(stack) > 0:
                    count += 1
                    elem = stack.pop()
                else:
                    return
                if count == k:
                    return elem.val
                
                next = elem.right


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(11)
root.right.right = TreeNode(30)
root.left.right = TreeNode(7)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(1)
root.left.left.right = TreeNode(4)

x = Solution().kthsmallest(root, 7)
print(x)