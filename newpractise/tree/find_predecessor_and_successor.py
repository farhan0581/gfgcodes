'''
Problem statement
You have been given a binary search tree of integers with ‘N’ nodes. You are also given 'KEY' which represents data of a node of this tree.



Your task is to return the predecessor and successor of the given node in the BST.



Note:
1. The predecessor of a node in BST is that node that will be visited just before the given node in the inorder traversal of the tree. If the given node is visited first in the inorder traversal, then its predecessor is NULL.

2. The successor of a node in BST is that node that will be visited immediately after the given node in the inorder traversal of the tree. If the given node is visited last in the inorder traversal, then its successor is NULL.

3. The node for which predecessor and successor are to be found will always be present in the given tree.

4. A binary search tree (BST) is a binary tree data structure which has the following properties.
     • The left subtree of a node contains only nodes with data less than the node’s data.
     • The right subtree of a node contains only nodes with data greater than the node’s data.
     • Both the left and right subtrees must also be binary search trees.


Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
https://files.codingninjas.in/screenshot-14-5921.png
15 10 20 8 12 16 25 -1 -1 -1 -1 -1 -1 -1 -1
10
Sample output 1:
8 12
Explanation of Sample output 1:
The tree can be represented as follows:

The inorder traversal of this tree will be 8 10 12 15 16 20 25.

Since the node with data 8 is on the immediate left of the node with data 10 in the inorder traversal, the node with data 8 is the predecessor.

Since the node with data 12 is on the immediate right of the node with data 10 in the inorder traversal, the node with data 12 is the successor.

APPROACH:
- find inorder traversal and use binary search to find the predecssor and successor of the key
- efficient is discussed below

'''
from os import *
from sys import *
from collections import *
from math import *

'''
    ------- Binary Tree node structure -------
            class   BinaryTreeNode :
                def __init__(self, data) :
                    self.data = data
                    self.left = None
                    self.right = None

                def __del__(self):
                    if self.left:
                        del self.left
                    if self.right:
                        del self.right
      
'''

def findpre(node, x, pre):
    if not node:
        return pre
    
    if x == node.data:
        # check if left there or not
        if node.left:
            pre = node.left.data
            # this is important, we need to find the next min , so go left -> right
            return findpre(node.left.right, x, pre)
        
    elif x > node.data:
        pre = node.data
        return findpre(node.right, x, pre)
    else:
        # still need to go deeper to find predecessor
        return findpre(node.left, x, pre)
    
    return pre
    

def findpos(node, x, pos):
    if not node:
        return pos

    if x == node.data:
        if node.right:
            pos = node.right.data
            return findpos(node.right.left, x, pos)
    elif x < node.data:
        pos = node.data
        return findpos(node.left, x, pos)
    else:
        return findpos(node.right, x, pos)
    
    return pos



def predecessorSuccessor(root, key):
    pre = -1
    p = findpre(root, key, pre)
    pp = findpos(root, key, -1)
    return [p, pp]


