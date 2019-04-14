# Definition for a  binary tree node
class TreeNode:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    s = 0

    def traverse(self, node, num):
        if not node:
            return None
        num = num*10 + node.val
        

        if not node.left and not node.right:
            self.s = (self.s+num)%1003

        left = self.traverse(node.left, num)
        right = self.traverse(node.right, num)


    def sumNumbers(self, node):
        self.traverse(node, 0)
        return self.s


        # stack = []
        # num = 0
        # s = 0

        # while True:

        #     while node:
        #         stack.append(node)
        #         num = num*10 + node.val
        #         node = node.left

            
        #     if not stack:
        #         return
        #     pop = stack.pop()
        #     print(pop.val)
        #     node = pop.right

        #     # leaf
        #     if not pop.left and not pop.right:
        #         print(num)
        #         # print(stack)
        #         print('----------')
        #         s += num
        #     num = num // 10


root = TreeNode(2)
root.left = TreeNode(1)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.left.right.left = TreeNode(9)
root.right = TreeNode(4)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

print(Solution().sumNumbers(root))