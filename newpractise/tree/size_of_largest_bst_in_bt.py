
'''

    ------- Binary Tree node structure -------
            class TreeNode :
                def __init__(self, data) :
                    self.data = data
                    self.left = None
                    self.right = None

'''

'''

logic : max(all elements in left subtree) < node < min(all elements in right subtree)
postorder travrsal because we need to compute left and right before the root

'''

INT_MIN = -99999999
INT_MAX = 99999999

def traverse(node, size, m1, m2): # m1 = minrange m2 = maxrange
    if not node:
        return 0,INT_MAX,INT_MIN
    
    # if node and not node.left and not node.right:
    #     return 1, node.data, node.data
    
    sizeLeft, minl, maxl = traverse(node.left, size, m1, m2)
    sizeRight, minr, maxr = traverse(node.right, size, m1, m2)

    if node.data > maxl and node.data < minr:
        return 1 + sizeLeft + sizeRight, min(node.data, minl), max(node.data, maxr)
    
    return max(sizeLeft, sizeRight), INT_MIN, INT_MAX

    

def largestBST(root):
    size, x,y = traverse(root, 0 , INT_MAX,INT_MIN)
    return size
	