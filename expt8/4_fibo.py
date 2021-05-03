def fibon(n):
    a = 0
    b = 1
    sum = 0
    count = 1
    print("Fibonacci Series: ", end = " ")
    while(count <= n):
        print(sum, end = " ")
        count += 1
        a = b
        b = sum
        sum = a + b

if __name__ == '__main__':
    fibon(12)
    # fibon(1000)