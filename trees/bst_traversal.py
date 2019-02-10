class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = []
        self.push_elem(root)


    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if len(self.stack) > 0:
            return True
        return False

    # @return an integer, the next smallest number
    def next(self):
        elem = self.stack.pop()
        if elem.right:
            self.push_elem(elem.right)
        return elem.val


    def push_elem(self, node):
        while node:
            self.stack.append(node)
            node = node.left

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(11)
root.right.right = TreeNode(30)
root.left.right = TreeNode(7)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(1)
root.left.left.right = TreeNode(4)

# Your BSTIterator will be called like this:
i = BSTIterator(root)
while i.hasNext(): print (i.next())