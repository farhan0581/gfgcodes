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

# basically params are initialized once
def test(a, b=[]):
	for i in range(a):
		b.append(i)
	print(b)

# test(2)
# test(3, [])
# test(4)


class Test(object):
	def __init__(nitin):
		print('in parent')
	
class Test1(Test):
	def __init__(kk, name):
		kk.name = name
		print('in child')
	
	def test(bla):
		print(bla.name)

obj = Test1('farhan')
obj.test()