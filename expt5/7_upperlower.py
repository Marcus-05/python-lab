def upper_lower(name):
    upper_count = 0
    lower_count = 0

    for i in name:
        if i.islower():
            lower_count += 1

        if i.isupper():
            upper_count += 1
    return upper_count, lower_count


name = input("Enter any string : ")
uppercount, lowercount = upper_lower(name)
print(f"uppercount {uppercount} lowercount {lowercount}")
