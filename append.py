name = {
    'a': 1,
    'd': 4,
    'e': 5,
    'b': 2,
    'c': 3,
}
print(name)
sort = sorted(name.keys())
print(sort)
for i in sort:
    print(i + '-' + str(name[i]))
