'''
Problem statement
You are given a binary tree having 'n' nodes. Each node of the tree has an integer value.



Your task is to find the maximum possible sum of a simple path between any two nodes (possibly the same) of the given tree.



A simple path is a path between any two nodes of a tree, such that no edge in the path is repeated twice. The sum of a simple path is defined as the summation of all node values in a path.

Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
1 2 3 4 -1 -1 -1 -1 -1
Sample Output 1:
10
Explanation For Sample Input 1:
The tree looks as follows:
                        1
                       / \
                      2   3 
                     /
                    4
The path between Node 3 (with value 3) and Node 4 (with value 4) produces the maximum sum, i.e., 10. Hence, the maximum possible sum is 10 in this case.
Sample Input 2:
2 4 -1 3 6 -1 -1 -1 -1 
Sample Output 2:
13
Explanation For Sample Input 2:
The tree looks as follows:
                        2
                       / 
                      4    
                     / \   
                    3   6
The path between Node 3 (with value 3) and Node 4 (with value 6) produces the maximum sum, i.e., 13. Hence, the maximum possible sum is 13 in this case.
Expected time complexity:
 The expected time complexity is O(n).
Constraints:
1 <= 'n' <= 10^6
-10^5 <= 'data' <= 10^5 and 'data' !=-1

Where ‘n’ is the total number of nodes in the binary tree, and 'data' is the value of the binary tree node

Time Limit: 1 sec

APPROACH:
- at every node we need to compute the leftsum(leftsubtree) and rightsum(rightsubtree)
- then at a node the sum = node.val + leftsum + rightsum
- but we need to return only the max of (left, right)

'''
# Following is the TreeNode class structure.
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def traverse(node, s):
    if not node:
        return 0,s

    leftsum,s = traverse(node.left,s)
    rightsum,s = traverse(node.right,s)

    if leftsum < 0:
        leftsum = 0
    
    if rightsum < 0:
        rightsum = 0

    s = max(s, node.data+leftsum+rightsum) # keep track of maxsum 

    return node.data + max(leftsum, rightsum),s # this gives max sum from whichever subtree





def maxPathSum(root: BinaryTreeNode) -> int:
    # Write your code here.
    s = -99999999999
    x,y = traverse(root, s)
    return y