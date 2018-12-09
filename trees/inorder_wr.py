class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.val = value



def inorder_traversal(tree):
    current = tree
    values = []
    stack = []

    while True:
        if current:
            stack.append(current)
            current = current.left
        
        else:
            if len(stack) > 0:
                _v = stack.pop()
                values.append(_v.val)
                current = _v.right
            else:
                return values
    
    return values
    







root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

# x = inorder_traversal(root)
# print(x)