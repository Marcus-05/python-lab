size = int(input("Enter the size of list : "))
print(f"Enter {size} elements ")
list = []

for i in range(0, size):
    list.append(int(input()))

for item in list:
    while(list.count(item) >= 2):
        list.remove(item)
list.sort()
print(list)
