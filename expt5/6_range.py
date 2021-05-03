def in_range(num, range1, range2):
    if range1 < num and range2  > num:
        return True
    else:
        return False

range1 = 0
range2 = 10
num = int(input("Enter the number :"))
if(in_range(num, range1, range2)):
    print("I range")
else:
    print("not in range")
