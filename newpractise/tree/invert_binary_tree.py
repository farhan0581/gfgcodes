'''
Given the root of a binary tree, invert the tree, and return its root.

https://assets.leetcode.com/uploads/2021/03/14/invert1-tree.jpg

Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

https://assets.leetcode.com/uploads/2021/03/14/invert2-tree.jpg
Example 2:
Input: root = [2,1,3]
Output: [2,3,1]
Example 3:

Input: root = []
Output: []

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        q = [root]

        if not root:
            return root

        while q:
            node = q.pop()
            node.left, node.right = node.right, node.left

            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
            
                
        
        return root


        