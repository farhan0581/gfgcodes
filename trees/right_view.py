class Node:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

def _right_view(node, max_level, level):
    if not node:
        return max_level

    if max_level != None and max_level < level:
        print(node.val)
        max_level += 1
    
    max_level = _right_view(node.right, max_level, level+1)
    max_level = _right_view(node.left, max_level, level+1)


    return max_level

def right_view(node):
    _right_view(node, 0, 1)


root = Node(1)
# root.left = Node(2)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.left.right.right = Node(8)
# root.left.right.right.left = Node(9)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)
right_view(root)