def armstrong(num):
    num1 = str(num)
    sum = 0
    for i in range(0, len(num1)):
        temp = int(num1[i])
        sum += temp**3
    print(sum)
    if num == sum :
        return "is armstrong"
    else : 
        return "not armstrong"


num = int(input("Enter any number : "))

print("The given number is "+ armstrong(num))
