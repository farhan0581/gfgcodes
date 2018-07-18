# using decorators in python

def check(some_function, **kwargs):
	def test(*args, **kwargs):
		print('called')
		print(args, kwargs)
		some_function(*args, **kwargs)
		print('end')
	return test


var = 'test'
@check(url='undefined')
def tcheck(var, **kwargs):
	print('this is hello world')

tcheck(var, key='value')