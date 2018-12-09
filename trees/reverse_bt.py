from preorder_wr import preorder_traversal

class Node:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


def invertTree(node):
    # leaf
    if not node.left and not node.right:
        return node
    else:
        temp = invertTree(node.right)
        node.right = invertTree(node.left)
        node.left = temp
    return node



root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
itree = invertTree(root)
x = preorder_traversal(itree)
print(x)
