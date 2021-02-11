import pprint
message = 'I am a Good girl'

count = {}

for character in message.upper():
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)

count['add'] = 'text'
pprint.pprint(count)
