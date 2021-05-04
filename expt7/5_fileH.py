# 5.Python program to read a file line by line and store it into a list.

def store_list(filename):
    with open(filename) as f:
        list = f.read().splitlines()
        print(list)

if __name__ == '__main__':
    store_list('test.txt')