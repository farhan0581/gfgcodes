class FindFreq(object):
	"""docstring for FindFreq"""
	def __init__(self, *args):
		self.arr = args[0]
		self.elem = args[1]

	def first_occurance(self, start, end):
		mid = (start + end) / 2
		
		if start <= end:

			if self.arr[mid] == self.elem and (mid==0 or self.arr[mid-1] < self.elem):
				return mid
			
			elif self.arr[mid] < self.elem:
				return self.first_occurance(mid+1, end)

			else:
				return self.first_occurance(start, mid-1)
		else:
			return -1


	def last_occurance(self, start, end):
		mid = (start + end) / 2
		
		if start <= end:

			if self.arr[mid] == self.elem and (mid==len(self.arr)-1 or self.elem < self.arr[mid+1]):
				return mid
			
			elif self.arr[mid] < self.elem:
				return self.last_occurance(mid+1, end)

			elif self.arr[mid] > self.elem:
				return self.last_occurance(start, mid-1)
		else:
			return -1

	def find(self):
		first = self.first_occurance(0, len(self.arr)-1) 
		if first != -1:
			last = self.last_occurance(first, len(self.arr)-1)
			print(first, last)



arr = [1,1,2,2,2,2,3,3,3]
obj = FindFreq(arr, 2)
obj.find()
 
