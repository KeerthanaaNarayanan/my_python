import random

print("Enter your name: ")
name = input()

print("Well, " + name + " I am thinking of a number between 1 and 20 You get 5 chance to find it here you go!")
secret = random.randint(1, 20)
find = False
for i in range(5):
    print('enter a number: ')
    given = int(input())
    if given < secret:
        print('its a bigger number')
    if given > secret:
        print('its a smaller number')
    if given == secret:
        print('holaa! you are correct')
        find = True
        break
if find is False:
    print('You didnt find the answer, it is ' + str(secret))