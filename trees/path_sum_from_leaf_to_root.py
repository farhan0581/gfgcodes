# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    result = []
    def traverse(self, node, k, s, path):
        # print(k,s, path)
        if not node:
            return None
        
        path.append(node.val)
        s += node.val
        
        if not node.right and not node.left and k == s:
            self.result += [path[:]]

        lpath = path[:]
        rpath = path[:]

        left = self.traverse(node.left, k, s, path)
        right = self.traverse(node.right, k, s, path)
        path.pop()

    def pathSum(self, node, k):
        self.traverse(node, k, 0, [])
        res = self.result
        self.result = []
        return res


root = TreeNode(2)
root.left = TreeNode(1)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.left.right.left = TreeNode(7)
root.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(Solution().pathSum(root, 13))