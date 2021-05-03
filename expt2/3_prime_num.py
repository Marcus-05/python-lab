import sympy


i, f = input("Enter the interval : ").split(" ")
i = int(i)
f = int(f)



for prime in range (i,f+1):
    if (sympy.isprime(prime)):
        print(prime)

