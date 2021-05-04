# 7.python program to find the longest words. 
def longest_word(filename):
    with open(filename) as f:
        words = f.read().split()
        print(max(words))

if __name__ == '__main__':
    print(longest_word('test.txt',9))
