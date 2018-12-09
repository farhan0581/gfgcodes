class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.val = value


def preorder_traversal(tree):
    stack = [tree]
    values = [tree.val]
    current = tree

    while True:
        
        if current and current.left:
            current = current.left
            stack.append(current)
            values.append(current.val)
        # else current and current.right:
            # current = current.right
        else:
            if len(stack) > 0:
                p = stack.pop()
                current = p.right
                if current:
                    values.append(current.val)
                    stack.append(current)
            else:
                return values
    return values

# root = Node(1)
# root.left = Node(2)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right = Node(3)
# root.right.left = Node(6)
# root.right.right = Node(7)

# x = preorder_traversal(root)
# print(x)