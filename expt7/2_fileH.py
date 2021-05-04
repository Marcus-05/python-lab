#2.Python program to read first n lines of a file.
from itertools import islice
def read_n_lines(filename,n):
    with open(filename) as f:
        for line in islice(f,n):
            print(line)


if __name__ == '__main__':
    read_n_lines("test.txt",3)