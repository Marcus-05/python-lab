size = int(input("Enter the size of list : "))
print(f"Enter {size} elements ")
list = []
for i in range(0, size):
    list.append(int(input()))
print(f"The max element in the list is {min(list)}")
