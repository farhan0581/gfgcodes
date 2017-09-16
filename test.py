# using decorators in python

def check(some_function):
	def test(*args, **kwargs):
		print 'called'
		print args, kwargs
		some_function(*args, **kwargs)
		print 'emd'
	return test


var = 'test'
@check
def tcheck(var,**kwargs):
	print 'this is hello world'

tcheck(var, key="value")