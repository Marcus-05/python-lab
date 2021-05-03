size = int(input("Enter the size of list : "))
print(f"Enter {size} elements ")
list = []
for i in range(0,size):
    list.append(int(input()))
print(f"The sum of all elements of list is {sum(list)}")