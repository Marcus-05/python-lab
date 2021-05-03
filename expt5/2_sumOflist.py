def sum_list(list):
    return sum(list)


list = [i for i in range(11)]
print(list)

list1 = [j for j in range(11) if j % 2 == 0]
print(list1)

print(f"The sum is {sum_list(list)}")
print(f"The sum is {sum_list(list1)}")
