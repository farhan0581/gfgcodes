'''
Problem statement
A binary tree is a tree where each node has at most two children i.e left child and right child.

You are given a binary tree, where the structure of the node is as follow -:

class BinaryTreeNode {
 int data;      // Value of the node.
 BinaryTreeNode *left;  // Pointer to left child node.
 BinaryTreeNode *right; // Pointer to right child node.
 BinaryTreeNode *next;  // Pointer to next right node at same level. 
}
Your task is to connect all the adjacent nodes at the same level in the given binary tree. You can do this by populating each 'next' pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL. Initially, all the next pointers are set to NULL.

For Example:

Consider the figure shown below. The left part represents the initial binary tree and right part represents the binary tree after connecting adjacent nodes at the same level.

In the tree shown in the picture above -:
The ‘next’ pointer of the node having value 2 is connected to the node having value 3.
The ‘next’ pointer of the node having value 4 is connected to the node having value 5.
The ‘next’ pointer of the node having value 5 is connected to the node having value 6.
The ‘next’ pointer of nodes having value 1, 3, 6 will have a value NULL as there are no next right nodes in their cases.
Note:

1. The structure of the ‘Node’ of a binary tree is already defined. You should not change it.   
2. The root of the binary tree is known to you.  
3. There is at least one node in the given binary tree.
4. You may only use constant extra space.
'''
from os import *
from sys import *
from collections import *
from math import *

'''
    ----------------- Binary Tree node class for reference -----------------
    
    class BinaryTreeNode:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
            self.next = None
'''
# using level order traversal
def connectNodes(root):
    
    q = [root]

    while len(q) > 0:
        
        size = len(q)
        prev = q[0]

        for i in range(size):
            node = q.pop(0)
            if i > 0 and i < size:
                prev.next = node
                prev = node
            
            if node.left:
                q.append(node.left)
            
            if node.right:
                q.append(node.right)
    
    return root

        