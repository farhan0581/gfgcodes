from tree_inorder import TreeNode

class Tree:
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Tree(TreeNode):
	"""docstring for Tree"""
	def __init__(self, value):
		super(Tree, self).__init__(value)
		self.height = 0

	def findHeight(self):
		if self is None:
			return 0
		lheight = rheight = 0	
		if self.left:
			lheight = self.left.findHeight()
		if self.right:
			rheight = self.right.findHeight()
		return max(lheight, rheight) + 1



def minDepth(node):
	if not node:
		return 0
	return 1 + min(minDepth(node.left), minDepth(node.right))


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
# root.right.left = Tree(4)
# root.right.left.right = Tree(5)

print(minDepth(root))



