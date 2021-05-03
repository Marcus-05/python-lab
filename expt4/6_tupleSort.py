list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]


def last(n):
    return n[-1]


def sort(tuples):
    return sorted(tuples, key = last)


print("Sorted:")
print(sort(list))
