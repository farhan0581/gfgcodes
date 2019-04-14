# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def check(self, root1, root2):
        if not root1 and not root2:
            return True
        
        if root1 and root2 and root1.val == root2.val and self.check(root1.left, root2.right) and self.check(root1.right, root2.left):
            return True
        
        return False

    def isSymmetric(self, node):
        return self.check(node.left, node.right)




root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(5)
# root.right.right = TreeNode(4)

print(Solution().isSymmetric(root))
