import sympy


num = int(input("Enter the number :"))

if(sympy.isprime(num)):
    print("The number is prime!!")
else : 
    print("The number is not prime")