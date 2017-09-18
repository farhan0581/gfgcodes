class TreeNode(object):
	def __init__(self, value):
		self.data = value
		self.left = None
		self.right = None

	def findLcs(self, node1, node2):
		if self:
			if node1 <= self.data <= node2:
				print("LCS is %s") % (self.data)
				return
			elif node1 > self.data and node2 > self.data:
				self.right.findLcs(node1, node2)
			elif node1 < self.data and node2 < self.data:
				self.left.findLcs(node1, node2)
			else:
				print 'here'

	def findLcsNonBST(self, node1, node2):

		if self.data == node1 or self.data == node2:
			return self

		rlcs = llcs = None
		
		if self.right is not None:
			rlcs = self.right.findLcsNonBST(node1, node2)
		if self.left is not None:
			llcs = self.left.findLcsNonBST(node1, node2)

		if rlcs and llcs:
			return self

		return rlcs if rlcs is not None else llcs

		

	def inorder(self):
		if self.left:
			self.left.inorder()
		print self.data
		if self.right:
			self.right.inorder()


root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(20)
root.right.left = TreeNode(11)
root.right.right = TreeNode(30)
root.left.right = TreeNode(7)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(1)
root.left.left.right = TreeNode(4)
root.findLcs(11, 30)

# for non bst
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

lcs = root.findLcsNonBST(4,7)
print lcs.data