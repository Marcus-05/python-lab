list = ['a', "aba", "bab", "b", "Nitin", "MOM"]

count = 0
for item in list:
    if len(item) < 2:
        continue
    else:
        if item[0].lower() == item[-1].lower():
            count += 1


print(f"The count is {count}")
