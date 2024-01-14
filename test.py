# class Node:
#     def __init__(self, value):
#         self.right = None
#         self.left = None
#         self.val = value


# def preorder_traversal(node):
#     stack = []
#     values = []
#     # current = node

#     while True:
        
#         if node:
#             values.append(node.val)
#             stack.append(node)
#             node = node.left
            
            
#         # else current and current.right:
#             # current = current.right
#         else:
#             if len(stack) > 0:
#                 _node = stack.pop()
#                 node = _node.right
#                 # if current:
#                 #     values.append(current.val)
#                 #     stack.append(current)
#             else:
#                 return values
#     return values

# root = Node(1)
# root.left = Node(2)
# root.left.left = Node(4)
# root.left.right = Node(5)
# root.right = Node(3)
# root.right.left = Node(6)
# root.right.right = Node(7)

# x = preorder_traversal(root)
# print(x)
from ast import Add
from functools import partial


def add(name, a,b):
    print("we are doing", name)
    sum = a + b
    return sum


addx = partial(add, "add", 1)
print(addx(2))
print(addx(3))
print(addx(33))