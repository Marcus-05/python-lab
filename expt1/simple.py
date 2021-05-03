# formula =  A = P(1+rt) 
'''
A	=	final amount
P	=	initial principal balance
r	=	annual interest rate
t	=	time (in years)
'''

P = int(input("Enter the initial priciple : "))
r = int(input("Enter the annual rate  : "))
t = int(input("Time in year : "))
A = P*(1+r*t)
print("Simple intrest is : {A}")
