class FindFreq(object):
	"""docstring for FindFreq"""
	def __init__(self, *args):
		self.arr = args[0]
		self.elem = args[1]

	def first_occurance(self, start, end):
		mid = (start + end) / 2
		
		if self.arr[mid] == self.elem and (mid==0 or self.arr[mid-1] < self.elem):
			return mid
		
		elif self.arr[mid] < self.elem:
			return self.first_occurance()




	def last_occurance(self, arr, start, end, elem):
		pass
		