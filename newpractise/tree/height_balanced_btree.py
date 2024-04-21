'''
Problem statement
You are given the root node of a binary tree.



Return 'true' if it is a height balanced binary tree.



Note:
Height of a tree is the maximum number of nodes in a path from the node to the leaf node.

An empty tree is a height-balanced tree. A non-empty binary tree is a height-balanced binary tree if
1. The left subtree of a binary tree is already the height-balanced tree.
2. The right subtree of a binary tree is also the height-balanced tree.
3. The difference between heights of left subtree and right subtree must not more than ‘1’.
'''
# Following is the TreeNode class structure.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def findheight(node):
    if not node:
        return 0
    
    return 1 + max(findheight(node.left), findheight(node.right))

# bruteforce
def traverse2(node):
    if not node:
        return True
    
    height_left = findheight(node.left)
    height_right = findheight(node.right)

    if abs(height_left-height_right) <= 1 and traverse(node.left) and traverse(node.right):
        return True
    
    return False


# covnvert height function to return -1 in case there is some issue
def traverse(node):
    if not node:
        return 0
    
    lt = traverse(node.left)
    rt = traverse(node.right)

    if lt == -1 or rt == -1:
        return -1
    
    if abs(lt-rt) > 1:
        return -1

    return 1 + max(lt, rt)


def isBalancedBT(root: BinaryTreeNode) -> bool:
    # Write your code here.
    
    ans = traverse(root)
    if ans == -1:
        return False
    return True




