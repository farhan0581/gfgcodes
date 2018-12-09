class Node:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.val = value

# using 2 stacks
def postorder_traversal(tree):
    current = tree
    stack1 = []
    stack2 = []

    current = tree
    stack1.append(current)
    next = tree
    while len(stack1) > 0:
        p = stack1.pop()
        stack2.append(p.val)
        # current = p

        if p and p.left:
            stack1.append(p.left)
            next = p.left
        if p and p.right:
            stack1.append(p.right)
            next = p.right
        current = next
    
    return stack2[::-1]


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)
root.right.left = Node(6)
root.right.right = Node(7)

x = postorder_traversal(root)
print(x)


