'''
You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

Each minute, a node becomes infected if:

The node is currently uninfected.
The node is adjacent to an infected node.
Return the number of minutes needed for the entire tree to be infected.

 

Example 1:

https://assets.leetcode.com/uploads/2022/06/25/image-20220625231744-1.png
Input: root = [1,5,3,null,4,10,6,9,2], start = 3
Output: 4
Explanation: The following nodes are infected during:
- Minute 0: Node 3
- Minute 1: Nodes 1, 10 and 6
- Minute 2: Node 5
- Minute 3: Node 4
- Minute 4: Nodes 9 and 2
It takes 4 minutes for the whole tree to be infected so we return 4.
Example 2:


Input: root = [1], start = 1
Output: 0
Explanation: At minute 0, the only node in the tree is infected so we return 0.
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createGraph(self, root):
        adj = {}
        q = [root]
        
        while len(q) > 0:
            node = q.pop(0)
            
            if node.left:
                tmp = adj.get(node.val, [])
                tmp.append(node.left.val)
                adj[node.val] = tmp

                tmp = adj.get(node.left.val, [])
                tmp.append(node.val)
                adj[node.left.val] = tmp

                q.append(node.left)
                
            if node.right:
                tmp = adj.get(node.val, [])
                tmp.append(node.right.val)
                adj[node.val] = tmp

                tmp = adj.get(node.right.val, [])
                tmp.append(node.val)
                adj[node.right.val] = tmp

                q.append(node.right)
        
        return adj




    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        adj = self.createGraph(root)
        q = [(start, 0)]
        vis = {}
        ans = 0

        while len(q) > 0:
            node, dis = q.pop(0)
            vis[node] = 1
            ans = max(ans, dis)
            for adjNode in adj.get(node, []):
                visited = vis.get(adjNode, 0)
                if visited == 0:
                    q.append((adjNode, dis+1))
                    vis[adjNode] = 1
        return ans


