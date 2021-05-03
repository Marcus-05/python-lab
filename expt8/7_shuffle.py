"""
Write a Python program to shuffle numbers from the given list n=[15,20 38, 45,10,5]
using random module.
"""
from random import shuffle

if __name__ == '__main__':
    n = [15, 20, 38, 45, 10, 5]
    shuffle(n)
    print(n)
