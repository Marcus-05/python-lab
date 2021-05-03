size = int(input("Enter the size of list : "))
print(f"Enter {size} elements ")
list = []

mult = 1
for i in range(0,size):
    list.append(int(input()))
    mult*=list[i]


print(f"The mul of all list member is {mult}")