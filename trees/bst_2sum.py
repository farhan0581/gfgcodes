# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer

    def reverse_inorder(self, node):
        if not node:
            return None
        
        self.reverse_inorder(node.right)
        return node.val
        self.reverse_inorder(node.left)
    
    def inorder(self, node):
        
        stack = []

        while True:

            while node:
                stack.append(node)
                node = node.left
            
            if not stack:
                return
            pop = stack.pop()
            print(pop.val)
            node = pop.right

    def check(self, node, sum, k):
        if not node:
            return 0
        sum += node.val
        if sum == k:
            return 1
        elif sum > k:
            return 0
        
        else:
            self.check(node.left, sum, k)
            self.check(node.right, sum, k)
        
        return 0


    def t2Sum(self, node, k):
        inorder = rinorder = True
        stack_i = []
        stack_r = []
        rnode = node

        val1 = val2 = None

        while True:
            if inorder:
                while node:
                    stack_i.append(node)
                    node = node.left
                
                if stack_i:
                    pop = stack_i.pop()
                    val1 = pop
                    node = pop.right
                    inorder = False
            
            if rinorder:
                while rnode:
                    stack_r.append(rnode)
                    rnode = rnode.right
                
                if stack_r:
                    pop = stack_r.pop()
                    val2 = pop
                    rnode = pop.left
                    rinorder = False
            
            if val1 == val2:
                return 0

            s = val1.val + val2.val

            if s == k and val1 != val2:
                return 1
            
            elif s < k:
                inorder = True

            elif s > k:
                rinorder = True



root = TreeNode(20)
root.left = TreeNode(10)
root.left.left = TreeNode(5)
root.left.right = TreeNode(15)
root.right = TreeNode(40)
root.right.left = TreeNode(30)
root.right.right = TreeNode(50)

# x = Solution().inorder(root)
print(Solution().t2Sum(root, 60))
