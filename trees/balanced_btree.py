# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None
    
    def __str__(self):
        return "node:%s" % self.val

class Solution:
    # @param A : root node of tree
    # @return an integer

    def find_height(self, node):
        # print(node)
        if not node:
            return 0
        
        hleft = 1 + self.find_height(node.left)
        hright = 1 + self.find_height(node.right)

        return max(hleft, hright)

    def isBalanced(self, node):
        if not node:
            return 1

        hleft = self.find_height(node.left)
        hright = self.find_height(node.right)

        if abs(hleft-hright) <= 1 and self.isBalanced(node.left) and self.isBalanced(node.right):
            return 1

        return 0

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
# root.left.left.left = TreeNode(5)

print(Solution().isBalanced(root))