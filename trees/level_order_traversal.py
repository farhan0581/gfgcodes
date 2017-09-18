from tree_inorder import TreeNode
import time

class Tree(TreeNode):
	"""docstring for Tree"""
	def __init__(self, value):
		super(Tree, self).__init__(value)
		self.queue = []

	def levelOrder(self):
		if self is None:
			return None

		self.queue.append(self)
		print self.value
		print self.queue

		# take a queue and store the values in it

		while len(self.queue) > 0:
			node = self.queue[0]
			print node.value
			del self.queue[0]
			print self.queue

			if node.left:
				self.queue.append(node.left)
			if node.right:
				self.queue.append(node.right)


		
root = Tree(10)
root.left = Tree(9)
root.right = Tree(21)
root.left.left = Tree(7)
root.right.right = Tree(34)

root.levelOrder()

