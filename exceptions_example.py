

class OopsException(Exception):
	pass

try:
	print("Hope we don't get an oops")
	raise OopsException()

except OopsException:
	print('Oh well ... Caught an oops')





