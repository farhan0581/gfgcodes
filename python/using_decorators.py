# using decorators in python

def check(**kwargs):
	def _check(some_function):
		def test(*args, **kwargs):
			print('called')
			print(args, kwargs)
			some_function(*args, **kwargs)
			print('end')
		return test
	return _check


var = 'test'
@check(url='undefined')
def tcheck(var, **kwargs):
	print('this is hello world')

tcheck(var, key='value')