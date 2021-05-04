# 1.Write a Python program to read an entire text file.
def read_file(filename):
    with open(filename) as pointer:
        print(pointer.read())


if __name__ == '__main__':
    read_file("test.txt")