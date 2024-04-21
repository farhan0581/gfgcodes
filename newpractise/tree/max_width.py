
'''
https://takeuforward.org/data-structure/maximum-width-of-a-binary-tree/
we take care of the index only
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return []
        q = [(root, 0)]
        m = {}
        

        maxwidth = 0

        while len(q) > 0:
            
            size = len(q)
            min_ind = q[0][1]
            m1 = min_ind
            m2 = min_ind
            for i in range(size):
                node, ind = q.pop(0)

                new_ind = ind-min_ind

                if i == 0:
                    m1 = ind
                
                if i == size-1:
                    m2 = ind

                if node.left:
                    q.append((node.left, 2*new_ind+1))
                
                if node.right:
                    q.append((node.right, 2*new_ind+2))
            
            maxwidth = max(maxwidth, m2-m1+1)

        return maxwidth

        return []