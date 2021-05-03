

'''# Armstrong number 
userInput = int(input("Enter the Number : "))
# 153 = 1**3 + 5**3 + 3**3 == 153

n = len(str(userInput))
initialUserInput = userInput
armstrong = 0 
while ( userInput > 0):
    LastDigit = userInput % 10
    userInput = userInput // 10
    armstrong = LastDigit**n + armstrong

if (armstrong == initialUserInput):
    print("The Number is Armstrong")
else :
    print("The number is not Armstrong")
'''


