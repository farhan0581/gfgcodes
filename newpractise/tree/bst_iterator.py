from os import *
from sys import *
from collections import *
from math import *

'''
Binary tree node class for reference

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
'''
class BSTiterator:
    def __init__(self, root):
        # Complete the constructor function
        self.stack = []
        self.root = root
        self.cur = None
        self.goLeft(root)
    
    def goLeft(self, node):
        if not node:
            return
        
        self.cur = node

        while self.cur:
            self.stack.append(self.cur)
            self.cur = self.cur.left
        
        # if self.cur.right:
        #    self. cur = self.cur.right

    def next(self):
        if len(self.stack) > 0:
            node = self.stack.pop()
            val = node.data
            if node.right:
                self.goLeft(node.right)
            return val

    def hasNext(self):
        if len(self.stack) > 0:
            return True
        return False
        
'''
    Your BSTIterator object will be instantiated and called as such:
    BSTIterator iterator(root)
    while(iterator.hasNext()):
       print(iterator.next())
'''