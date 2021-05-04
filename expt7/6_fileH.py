# 6.Python program to read a file line by line store it into a variable

def linebyline(filename):
    with open(filename) as f:
        lines = f.readlines()
        print(lines)

if __name__ == '__main__':
    linebyline('test.txt')