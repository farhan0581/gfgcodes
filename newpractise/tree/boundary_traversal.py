'''
Problem statement
You are given a binary tree having 'n' nodes.

https://files.codingninjas.in/boundarytraversal-5149.png

The boundary nodes of a binary tree include the nodes from the left and right boundaries and the leaf nodes, each node considered once.



Figure out the boundary nodes of this binary tree in an Anti-Clockwise direction starting from the root node.



Example :
Input: Consider the binary tree A as shown in the figure:

Output: [10, 5, 3, 7, 18, 25, 20]

Explanation: As shown in the figure

The nodes on the left boundary are [10, 5, 3]

The nodes on the right boundary are [10, 20, 25]

The leaf nodes are [3, 7, 18, 25].

Please note that nodes 3 and 25 appear in two places but are considered once.
'''
'''
    Time Complexity: O(N)
    Space Complexity: O(N)

    Where N is the number of nodes in the Binary Tree.
'''

# Binary tree node class for reference.
# class BinaryTreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None



def is_leaf(node):
    if node and not node.left and not node.right:
        return True
    return False

def preorder(root):
    st = [root]
    res = []
    while len(st) > 0:
        node = st.pop()
        if is_leaf(node) : #leaf
            res.append(node.data)
        
        if node.right:
            st.append(node.right)
        
        if node.left:
            st.append(node.left)
    
    return res


def left(root):
    st = [root]
    res = []
    while len(st) > 0:
        node = st.pop()
        
        if not node or is_leaf(node):
            break
        
        if not is_leaf(node):
            res.append(node.data)

        if node.left:
            st.append(node.left)
        else:
            st.append(node.right)
    
    return res

def right(root):
    st = [root]
    res = []

    while len(st) > 0:
        node = st.pop()

        if not node or is_leaf(node):
            break

        if not is_leaf(node):
            res.append(node.data)
        
        if node.right:
            st.append(node.right)
        else:
            st.append(node.left)
    
    return res[::-1]


# Functions to traverse on each part.
def traverseBoundary(root):
    # Write your code here.
    l = left(root.left) # if I send root here and check in function node != root, it was not working
    leaf = preorder(root)
    r = right(root.right) # if I send root here and check in function node != root, it was not working
    # print(l)
    # print(leaf)
    # print(r)
    return [root.data] + l + leaf + r


'''
approach is simple:
- find left boundary
- find preorder traversal to find only leaves
- find right boundary
return the answer
'''