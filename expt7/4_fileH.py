# 4.Python program to read last n lines of a file
def read_lastLine(filename,n):
    with open(filename) as f:
        # Lst[ Initial : End : IndexJump ]
        lines = f.read().splitlines()
        start = len(lines) - 1
        end = start - n
        print(lines[start:end:-1])




if __name__ == '__main__':
    read_lastLine('test.txt',2)