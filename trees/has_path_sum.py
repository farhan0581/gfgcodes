# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    has = 0
    def traversal(self, node, k, s):
        # print(k,s)
        if not node:
            return None

        s += node.val

        if not node.right and not node.left and k == s:
            self.has = 1
            return
        self.traversal(node.left, k, s)
        self.traversal(node.right, k, s)


    def hasPathSum(self, node, k):
        self.has = 0
        self.traversal(node, k, 0)
        # self.has = 0
        return self.has

root = TreeNode(2)
root.left = TreeNode(1)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.left.right.left = TreeNode(7)
root.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(Solution().hasPathSum(root, 13))