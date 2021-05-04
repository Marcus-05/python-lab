# 3.Python program to append text to a file and display the text
def write_file(filename):
    with open(filename,"a") as f:
        f.write("\nThis line have been written")
    
    pointer = open(filename)
    print(pointer.read())

if __name__ == '__main__':
    write_file("test.txt")