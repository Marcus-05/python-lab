""" Write a Python program to generate random number between (1, 50) 
and to generate random character from the word “computer” using random module """

from random import randint,choice
if __name__ == '__main__':
    computer = "computer"
    print(randint(1,50))
    print(choice(computer))