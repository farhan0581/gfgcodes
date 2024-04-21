'''
Problem statement
You are given a 'Binary Tree'.



Return the bottom view of the binary tree.



Note :
1. A node will be in the bottom-view if it is the bottom-most node at its horizontal distance from the root. 

2. The horizontal distance of the root from itself is 0. The horizontal distance of the right child of the root node is 1 and the horizontal distance of the left child of the root node is -1. 

3. The horizontal distance of node 'n' from root = horizontal distance of its parent from root + 1, if node 'n' is the right child of its parent.

4. The horizontal distance of node 'n' from root = horizontal distance of its parent from the root - 1, if node 'n' is the left child of its parent.

5. If more than one node is at the same horizontal distance and is the bottom-most node for that horizontal distance, including the one which is more towards the right.


Example:
Input: Consider the given Binary Tree:
https://files.codingninjas.in/first-5997.jpg

Output: 4 2 6 3 7

Explanation:
Below is the bottom view of the binary tree.

1 is the root node, so its horizontal distance = 0.
Since 2 lies to the left of 0, its horizontal distance = 0-1= -1
3 lies to the right of 0, its horizontal distance = 0+1 = 1
Similarly, horizontal distance of 4 = Horizontal distance of 2 - 1= -1-1=-2
Horizontal distance of 5 = Horizontal distance of 2 + 1=  -1+1 = 0
Horizontal distance of 6 = 1-1 =0
Horizontal distance of 7 = 1+1 = 2

The bottom-most node at a horizontal distance of -2 is 4.
The bottom-most node at a horizontal distance of -1 is 2.
The bottom-most node at a horizontal distance of 0 is 5 and 6. However, 6 is more towards the right, so 6 is included.
The bottom-most node at a horizontal distance of 1 is 3.
The bottom-most node at a horizontal distance of 2 is 7.

Hence, the bottom view would be 4 2 6 3 7


APPROACH:
- is mein bas yaheeh hai ek map mein daalte raho, important hai level order traversal like bfs
isi liye queue use kari hai yahan, phirs level sort kar ke result return kar do

'''
from typing import List

# Following is the TreeNode class structure.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bottomView(root: BinaryTreeNode) -> List[int]:
    # Write your code here.
    
    m = {}
    st = [(root, 0)]

    if not root:
        return []

    while len(st) > 0:
        node, dis = st.pop(0)

        m[dis] = node.data

     
        if node.left:
            st.append((node.left, dis-1))

        
        if node.right:
            st.append((node.right, dis+1))
        
    # print(m)
    level = sorted(m.keys())

    res = []
    for l in level:
        res.append(m[l])
    return res


