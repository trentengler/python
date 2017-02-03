



def test(func):
	def new_function(*args, **kwargs):
		print('Start: ', func.__name__)
		print('Running function: ', func.__name__)
		print('Positional arguments: ', args)
		print('Keyword arguments: ', kwargs)
		result = func(*args, **kwargs)
		print('Result: ', result)
		print('End: ', func.__name__)
		return result
	return new_function

@test
def getodds():
	for i in ([nums for nums in range(11) if nums % 2 != 0]):
		print(i)
	return i



print(getodds())

print(type(getodds))
