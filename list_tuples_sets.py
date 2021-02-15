grades = [56, 45, 67, 98, 23, 56] #items can repeat in list
tuples_grades = (45, 36, 27, 17, 45, 17) #immutable, items can repeat
set_grades = {24, 34, 24, 56, 100, 100} #unique and unordered

print(grades)
print(tuples_grades)
print(set_grades)

#we cant reassign tuples but can add.
print(grades[0])
print(tuples_grades[0])
# print(set_grades[0]) throughs an error because it is unordered.

#add in lists by
grades = grades + [45]
#grades.add(99) no such attribute.
print(grades)

#add to tuples by
tuples_grades = tuples_grades + (100, )
#tuples_grades.add(105) no such attribute
print(tuples_grades)

#add in set by
set_grades.add(68)
set_grades.add(68)
#set_grades = set_grades + (109) unsupproted opperand.
print(set_grades)

Types_1 = [
        'none',
        'echo-reply',
        'destination-unreachable',
        'source-quench',
        'redirect', 'alternative-host',
        'echo-request', 'router-advertise',
        'router-solicit', 'time-exceeded',
        'parameter-problem', 'timestamp',
        'timestamp-reply', 'info-request',
        'info-reply', 'address-mask-request',
        'address-mask-reply', 'traceroute',
        'datagram-error', 'mobile-host-redirect',
        'mobile-registration-request', 'mobile-registration-reply',
        'domain-name', 'domain-name-reply'
    ]
Types_2 = Types_1.copy()
Types_2.append('test')
print(Types_1)
print(Types_2)