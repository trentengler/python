
guess_me = 7
start = 1

while True:

	if start < guess_me:
		print('Too Low')
	elif start == guess_me:
		print('Found It')
		break
	else:
		print('Oops')
		break
	start +=1
