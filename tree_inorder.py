class TreeNode(object):
	"""docstring for TreeNode"""
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def inorder(self):
		if self.left:
			self.left.inorder()
		print self.value
		if self.right:
			self.right.inorder()

	def postorder(self):
		if self.left:
			self.left.inorder()
		if self.right:
			self.right.inorder()
		print self.value



root = TreeNode(10)
root.left = TreeNode(9)
root.right = TreeNode(21)
root.left.left = TreeNode(7)
root.right.right = TreeNode(34)
root.inorder()
root.postorder()