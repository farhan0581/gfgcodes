from os import *
from sys import *
from collections import *
from math import *




import queue
import sys
sys.setrecursionlimit(10**6)

class BinaryTreeNode:
    
    def __init__(self, data):
        
        self.data = data
        self.left = None
        self.right = None
        

# the main logic is to carry range for each node, thats it
def traverse(node, m1,m2):
    
    if not node:
        return True
    
    if node.data >= m1 and node.data <= m2 and traverse(node.left, m1, node.data) and traverse(node.right, node.data, m2):
        return True
    
    return False
        


        
def validateBST(root):

    m1 = -9999999999
    m2 = 9999999999
    
    return traverse(root, m1, m2)


def buildLevelTree(levelorder):
    
    index = 0
    length = len(levelorder)
    
    if length<=0 or levelorder[0]==-1:
        return None
    
    
    root = BinaryTreeNode(levelorder[index])
    index += 1
    
    q = queue.Queue()
    q.put(root)
    
    while not q.empty():
        
        currentNode = q.get()
        leftChild = levelorder[index]
        index += 1
        
        if leftChild != -1:
            
            leftNode = BinaryTreeNode(leftChild)
            currentNode.left =leftNode
            q.put(leftNode)
            
        rightChild = levelorder[index]
        index += 1
        
        
        if rightChild != -1:
            
            rightNode = BinaryTreeNode(rightChild)
            currentNode.right =rightNode
            q.put(rightNode)
            
            
    return root
    

t = int(sys.stdin.readline().strip())
while t >0:
    
    
    li = list(map(int, sys.stdin.readline().strip().split(" ")))
    root = buildLevelTree(li)
    if (validateBST(root)):
        print('true')
    else:
        print('false')
    t = t -1



