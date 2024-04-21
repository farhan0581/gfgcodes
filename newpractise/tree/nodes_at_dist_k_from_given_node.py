'''
Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png

'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findParent(self, root):
        m = {root.val: None}
        q = [root]
        
        while len(q) > 0:
            node = q.pop(0)
            if node.left:
                q.append(node.left)
                m[node.left.val] = node
            if node.right:
                q.append(node.right)
                m[node.right.val] = node
        
        return m

    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        q = [(target, 0)]
        vis = {}
        vis[target.val] = 1
        ans = []

        parent_info = self.findParent(root)
        # print(parent_info)

        while len(q) > 0:
            node, dist = q.pop(0)
            if dist == k:
                # print(node.val, dist)
                ans.append(node.val)
                # vis[node.val] = 1
            vis[node.val] = 1

            
            if node.left and dist+1 <= k  and not vis.get(node.left.val, None):
                q.append((node.left, dist+1))
                
            if node.right and dist+1 <= k  and not vis.get(node.right.val, None):
                q.append((node.right, dist+1))
                # vis[node.right.val] = 1
            
            parent = parent_info[node.val]
            if parent and dist+1 <= k  and not vis.get(parent.val, None):
                q.append((parent, dist+1))
                # vis[parent.val] = 1
        
        return list(set(ans))


        