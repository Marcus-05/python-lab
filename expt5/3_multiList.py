import math
def multi_list(list):
    return math.prod(list)


list = [i for i in range(1,11)]
print(list)

list1 = [j for j in range(1,11) if j % 2 == 0]
print(list1)

print(f"The sum is {multi_list(list)}")
print(f"The sum is {multi_list(list1)}")
