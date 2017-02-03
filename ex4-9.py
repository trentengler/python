


def getodds():
	for i in ([nums for nums in range(11) if nums % 2 != 0]):
		yield i

count = 1
for num in getodds():
	if count == 3:
		print('The third number is: ', num)
		break
	count += 1

print(type(getodds))
