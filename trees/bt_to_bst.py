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


# root = Tree(1)
# root.left = Tree(2)
# root.right = Tree(3)
# root.left.left = Tree(4)
# root.left.right = Tree(5)
# root.right.left = Tree(6)
# root.right.right = Tree(7)
# l=[]
# root.inorder(l)
# l.sort()
# root.btToBst(l)
# x=[]
# root.inorder(x)
# print x

def lis(seq, m=0, decrease=False):
    seq = [m] + seq
    lng = [0]  # lis length for index i
    ptr = [-1] # lis previous pointer for index i
    for i in xrange(1, len(seq)):
        js = None
        if not decrease:                                                                  
            js = filter(lambda j: seq[j] < seq[i], xrange(i))                             
        else:
            js = filter(lambda j: seq[j] > seq[i], xrange(i))
        k = max(js, key=lng.__getitem__) if js else 0
        lng.append(lng[k] + 1)
        ptr.append(k)
    # dereference pointer and build lis.
    cs = []
    pos = lng.index(max(lng))                                                            
    while pos != 0:                                                                       
        cs.append(seq[pos])                                                               
        pos = ptr[pos]
    final_lis = list(reversed(cs))                                                                  
    print final_lis
    return len(final_lis)

a = [1,2,6,9,12,0,3,5]
b = [2,6,3,1,2,4,6,2,1]

print lis(a)
print lis(b)
