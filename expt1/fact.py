def fact (num) :
    if num == 1 :
        return 1 
    else :
        return num * fact(num -1)

num = int(input("Enter the Number : "))
print(f"The factorial is {fact(num)}")

