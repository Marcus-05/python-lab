tuple = (1, 2, 4, 2, 3, 4, 5, 5, 5, 5, 5, 5, 7, 7, 8)
repeated = []

for i in tuple:
    if tuple.count(i) > 1:
        if repeated.count(i) == 0:
            repeated.append(i)

print(repeated)
