names = []
def who_do_you_know():
	# people

	user_input = ''
	while (user_input == 'yes'):
		if user_input is not 'exit':
			user_input = input("enter your friend name, to close enter exit")
			names.append(user_input)
		print(names)

def ask_user():
	friends = input("enter your friend's name")
	for name in names:
		if name == friends:
			print("you know {}".format(friends))
		else:
			print("you dont know {}".format(friends))


