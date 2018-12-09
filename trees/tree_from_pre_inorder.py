from preorder_wr import preorder_traversal
from postorder_wr import postorder_traversal

class TreeNode:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.val = value


def buildTree(preorder, inorder):
    # print(preorder, inorder)
    if len(preorder) <= 0:
        return
        
    root_val = preorder[0]
    node = TreeNode(root_val)
    preorder.remove(root_val)
    if len(inorder) <= 1:
        # print('------------')
        # print(preorder, inorder)
        return node

    try:
        print(inorder)
        root_ind = inorder.index(root_val)
        print(root_ind)
        node.left = buildTree(preorder, inorder[:root_ind])
        node.right = buildTree(preorder, inorder[root_ind+1:])
        return node
    except Exception as e:
        print(str(e))
        return


inorder = [2,1,3]
preorder = [1,2,3]
preorder = [ 2, 1, 6, 5, 3, 4 ]
inorder = [ 5, 6, 1, 2, 3, 4 ]

tree = buildTree(preorder, inorder)
x = postorder_traversal(tree)
print('-----------------')
print(x)