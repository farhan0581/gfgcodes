# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def check(self, node1, node2):
        if not node1 and not node2:
            return 1
        elif not node1 or not node2:
            return 0
        
        if node1.val == node2.val and self.check(node1.left, node2.left) and self.check(node1.right, node2.right):
            return 1
        return 0
        

    def isSameTree(self, node1, node2):
        return self.check(node1, node2)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.right.right = TreeNode(5)
         
root2 = TreeNode(1)
root2.left = TreeNode(2)
root2.right = TreeNode(3)
root2.left.left = TreeNode(4)
# root2.right.right = TreeNode(9)

print(Solution().isSameTree(root, root2))