'''
Problem statement
You have been given a Binary Search Tree of integers. You are supposed to return the k-th (1-indexed) smallest element in the tree.



For example:
For the given binary search tree and k = 3

The 3rd smallest node is highlighted in yellow colour.   
Detailed explanation ( Input/output format, Notes, Images )
https://files.codingninjas.in/test-explaination-9984.png
Sample Input 1:
3
10 5 15 4 7 14 16 -1 -1 -1 -1 -1 -1 -1 -1
Sample Output 1:
7
Explanation of Sample Input 1:

The third-smallest node is 7.
https://files.codingninjas.in/binarytree-6171.png
Sample Input 2:
2
-2 -4 1 -5 -1 -1 -1 -1 -1
Sample Output 2:
-4
Explanation of Sample Input 2:
The second-smallest node is -4.
Constraints:
1 <= N <= 10000
1 <= K <= N
-10^8 <= data <= 10^8 and data != -1

Where ‘N’ is the total number of nodes in the binary search tree, ‘K’ is the given integer and “data” is the value of the binary search tree node.

Time Limit: 1sec
'''
from typing import Optional

class TreeNode:
    def __init__(self, data: int):
        self.data = data
        self.left = None
        self.right = None


def traverse(node, c, k, num):
    if not node:
        return c,k,num
    
    c,k,num=traverse(node.left,c,k,num)
    c += 1
    if c == k:
        num = node.data
        return c,k,num
    c,k,num=traverse(node.right, c,k,num)

    return c,k,num



    

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    
    # Write the code here.
    num = -999999999
    c,k,num = traverse(root, 0, k, num)
    return num
