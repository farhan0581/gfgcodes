# https://stackoverflow.com/questions/2776829/difference-between-pythons-generators-and-iterators
class SimpleGen(object):
	"""this class returns on generator object"""
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def __iter__(self):
		start = self.start
		while start <= self.end:
			yield start
			start += 1

obj = SimpleGen(1,10)
for i in obj:
	print i