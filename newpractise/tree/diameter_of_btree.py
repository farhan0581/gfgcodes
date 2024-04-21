'''
Problem statement
You are given a Binary Tree.
https://files.codingninjas.in/diameterexplaination-6262.png


Return the length of the diameter of the tree.



Note :
The diameter of a binary tree is the length of the longest path between any two end nodes in a tree.

The number of edges between two nodes represents the length of the path between them.
Example :
Input: Consider the given binary tree:

Output: 6

Explanation:
Nodes in the diameter are highlighted. The length of the diameter, i.e., the path length, is 6.
'''
# Following is the TreeNode class structure.
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def traverse(node, d):
    if not node:
        return 0,d
    
    left_s,d = traverse(node.left, d)
    right_s,d = traverse(node.right, d)

    d = max(d, left_s + right_s)

    return 1+max(left_s, right_s),d


def diameterOfBinaryTree(root: TreeNode) -> int:
    # Write your code here.
    if not root:
        return 0
    
    d = 0
    
    t,d=traverse(root, d)

    return d
    