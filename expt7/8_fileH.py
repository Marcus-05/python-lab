# 8.Python program to count the number of lines in a text file. 

def count_line_easy(filename):
    with open(filename) as f:
        lines = f.read()
        print(lines.count('\n')+1) 

def count_line(filename):
    with open(filename) as f:
        lines = f.readlines()
        print(len(lines))

if __name__ == '__main__':
    count_line_easy('test.txt')
    count_line('test.txt')