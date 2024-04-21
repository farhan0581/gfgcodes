from os import *
from sys import *
from collections import *
from math import *

'''

    Following is the Binary Tree Node structure:

    class  TreeNode :
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

class BSTIterator:
    def __init__(self, root):
        self.root = root
        self.cur1 = None
        self.cur2 = None
        self.stackIn = []
        self.stackRIn = []
        self.left(root)
        self.right(root)


    def left(self, node):
        if not node:
            return
        
        self.cur1 = node

        while self.cur1:
            self.stackIn.append(self.cur1)
            self.cur1 = self.cur1.left

    # this will be reverse inorder (right - node - left)
    def right(self, node):
        if not node:
            return
        
        self.cur2 = node

        while self.cur2:
            self.stackRIn.append(self.cur2)
            self.cur2 = self.cur2.right
    
    def getNextBig(self):
        if len(self.stackIn) > 0:
            node = self.stackIn.pop()
            if node.right:
                self.left(node.right)
            return node.data

    def getNextSmall(self):
        if len(self.stackRIn) > 0:
            node = self.stackRIn.pop()
            if node.left:
                self.right(node.left)
            return node.data
    
    def has1(self):
        if len(self.stackIn) > 0:
            return True
        return False
    
    def has2(self):
        if len(self.stackRIn) > 0:
            return True
        return False


def pairSumBST(root, k):
    it = BSTIterator(root)
    a = it.getNextBig()
    b = it.getNextSmall()
    
    while it.has1() and it.has2():
        if a + b == k:
            return True
        elif a+b < k:
            a = it.getNextBig()
        else:
            b = it.getNextSmall()
    
    return False




