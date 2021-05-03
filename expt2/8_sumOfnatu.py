def naturalSum(n) :
    sum = 0
    for i in range (1,n+1):
        sum += i**2
    return sum


n = int(input("Enter the value of n : "))
print(f"The sum is {naturalSum(n)}")
