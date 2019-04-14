# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    check = [0,0]

    def _lca(self, node, val1, val2):

        if not node:
            return None
        # print(self.check)
        if node.val == val1:
            self.check[0] = 1
        if node.val == val2:
            self.check[1] = 1


        if node.val == val1:
            return node
        if node.val == val2:
            return node
        
        left = self._lca(node.left, val1, val2)
        right = self._lca(node.right, val1, val2)

        if left and right:
            return node
        
        return left if left else right
    
    def find(self, node, k):
        if not node:
            return None
        
        if node.val == k:
            return node
        l=self.find(node.left, k)
        r=self.find(node.right, k)
        return l if l else r
    
    
    def lca(self, node, val1, val2):
        self.check = [0,0]
        r = self._lca(node, val1, val2)
        # print(self.check)
        # print(r.val)
        if self.check[0] and self.check[1] or (self.check[0] and self.find(r, val2) or (self.check[1] and self.find(r, val1))):
            return r.val
        return -1


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(Solution().lca(root, 2,5))