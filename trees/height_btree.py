from tree_inorder import TreeNode

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


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.left.left = Tree(7)
root.left.right = Tree(5)
print root.findHeight()






