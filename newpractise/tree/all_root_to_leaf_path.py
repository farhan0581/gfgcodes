
'''

Problem statement
You are given an arbitrary binary tree consisting of 'N' nodes numbered from 1 to 'N'. Your task is to print all the root to leaf paths of the binary tree.

A leaf of a binary tree is the node which does not have a left child and a right child.



For Example :
Given a binary tree :

All the root to leaf paths are :
1 2 4
1 2 5 
1 3
Note :

1. Two nodes may have the same value associated with it.
2. The root node will be fixed and will be provided in the function.
3. Note that the nodes in a path will appear in a fixed order. For example, 1 2 3 is not the same as 2 1 3.
4. Each path should be returned as a string consisting of nodes in order and separated by a space.
5. The path length may be as small as ‘1’.

https://files.codingninjas.in/screenshot-from-2020-11-06-15-04-33-5639.png

    Following is the class structure of the BinaryTreeNode class:

    class BinaryTreeNode:
        def __init__(self, data):

            self.data = data
            self.left = None
            self.right = None

'''

# used dfs here, just that i have popped when both left and right child
from typing import List

def dfs(node, res, t):
    if node:
        res.append(str(node.data))

    if node and not node.left and not node.right:
        t.append(" ".join(res))
        return
    
    

    if node.left:
        dfs(node.left, res, t)
        res.pop()
    
    if node.right:
        dfs(node.right, res, t)
        res.pop()

    return

def allRootToLeaf(root) -> List[str]:
    result = []
    t = []
    dfs(root, result, t)
    # print(t)
    # print("---------")
    return t

    

