'''
P(1+r/n)**(n*t)
A	=	final amount
P	=	initial principal balance
r	=	interest rate
n	=	number of times interest applied per time period
t	=	number of time periods elapsed
'''


P = int(input("Enter the initial priciple : "))
r = int(input("Enter the annual rate  : "))
t = int(input("Time in year : "))
n = int(input("Enter the value for n"))
A = P*(1+(r/n))**(n*t)


print("The compound intrest is {A}")

