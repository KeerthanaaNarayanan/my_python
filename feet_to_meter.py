phrase = "hello {}, today is {}"
sentence = phrase.format('robot', 'monday')
print(sentence)

# get input from user
input_1 = input("enter the area of your house in sqaure feet: ")
change = int(input_1)
sqaure_metres = change/10.8
print("{} square feet is {} square meter".format(input_1,sqaure_metres))

