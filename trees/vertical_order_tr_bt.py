# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def traversal(self, node, dist, h):
        if not node:
            return

        try:
            t = self.map[dist]
            t.append([node.val, h])
        except:
            self.map[dist] = [[node.val, h]]

        self.traversal(node.left, dist-1, h+1)
        self.traversal(node.right, dist+1, h+1)
    
    def _verticalOrderTraversal(self, node):
        # from collections import OrderedDict
        result = []
        self.map = {}
        self.traversal(node, 0, 0)
        # print(self.map)
        for key in sorted(self.map):
            temp = [b[1] for b in sorted(enumerate(self.map[key]),key=lambda i:i[1])]
            result.append(temp)
        return result
        # print(sorted(self.map, key=))
    
    def verticalOrderTraversal(self, node):
        m = {}
        result = []
        q = [(node, 0)]

        while True:
            if not q:
                break
            
            t = q[0]
            del q[0]

            try:
                m[t[1]].append(t[0].val)
            except:
                m[t[1]] = [t[0].val]
            finally:
                pass
            
            
            if t[0].left:
                q.append((t[0].left, t[1]-1))
            
            if t[0].right:
                q.append((t[0].right, t[1]+1))
        
        
        for key in sorted(m):
            result.append(m[key])
        return result

            

root = TreeNode(6)
root.left = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(5)
# root.left.right.left = TreeNode(7)
root.right = TreeNode(7)
# root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

print(Solution().verticalOrderTraversal(root))

