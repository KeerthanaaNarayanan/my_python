should_continue = True
if should_continue:
	print("Hello")

known_people = ["ken", "ben", "hari", "raji", "narayanan"]
person = input("Enter the person you know:")

#if person in known_people:
#	print("you know this person")

#if person not in known_people:
#	print("you dont know this person")

if person in known_people:
	print("you know {}!".format(person)) #substitute input to the output format is used
elif person == 'hariprasath':
	print("you know {} happy for you!".format(person))
else:
	print("you dont know {}!".format(person))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def even_numbers():
	evens = []
	for number in numbers:
		if number % 2 == 0:
			evens.append(number)
	return evens

print(even_numbers())