# Definition for a  binary tree node
# https://www.geeksforgeeks.org/flatten-a-binary-tree-into-linked-list/
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def traverse(self, node):
        if not node:
            return
        
        l = self.traverse(node.left)
        r = self.traverse(node.right)

        if r and l:
            temp = r
            node.right = l
            _t = node.right
            while _t.right:
                _t = _t.right

            _t.right = temp
        
        elif r and not l:
            node.right = r
        elif not r and l:
            node.right = l
        
        node.left = None
        return node
    
    def flatten(self, node):
        return self.traverse(node)
        return node
    
    def inorder(self, root):
        if not root:
            return None
        
        self.inorder(root.left)
        print(root.val)
        self.inorder(root.right)

root = TreeNode(1)
root.left = TreeNode(2)
# root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)
Solution().inorder(root)

print(Solution().flatten(root))
Solution().inorder(root)