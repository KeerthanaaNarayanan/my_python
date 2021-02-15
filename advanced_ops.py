class name1():
    # set operations
    ur_lottery = {6, 2, 3, 5}

    winning_numbers = {2, 3, 7, 8}

    # gives the intersection of two sets.
    print(ur_lottery.intersection(winning_numbers))

    # gives the union of two sets
    print(ur_lottery.union(winning_numbers))

    # gives the difference of the two sets
    print({5, 4, 6, 2}.difference({4, 5, 7, 8}))
    print(ur_lottery.difference(winning_numbers))
    print(winning_numbers.difference(ur_lottery))

    tuple_ex = (9)  # is not a tuple.
