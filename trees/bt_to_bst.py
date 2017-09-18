from tree_inorder import TreeNode

class Tree(TreeNode):
	"""docstring for Tree"""
	def __init__(self, value):
		super(Tree, self).__init__(value)
		self.temp = []


	def btToBst(self, inorder_tr):
		if self is None:
			return None

		if self.left:
			self.left.btToBst(inorder_tr)

		self.value = inorder_tr[0]
		del inorder_tr[0]

		if self.right:
			self.right.btToBst(inorder_tr)


	def inorder(self, temp):
		if self.left:
			self.left.inorder(temp)
		temp.append(self.value)
		if self.right:
			self.right.inorder(temp)


root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)
root.right.left = Tree(6)
root.right.right = Tree(7)
l=[]
root.inorder(l)
l.sort()
root.btToBst(l)
x=[]
root.inorder(x)
print x