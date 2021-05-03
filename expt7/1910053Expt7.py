
# 1.Write a Python program to read an entire text file.
def file_read(fname):
        txt = open(fname)
        print(txt.read())
file_read("test.txt") 

# 2.Python program to read first n lines of a file.
def file_read_from_head(fname, nlines):
        from itertools import islice
        with open(fname) as f:
                for line in islice(f, nlines):
                        print(line)
file_read_from_head('test.txt',2)


# 3.Python program to append text to a file and display the text
def file_read(fname):
        from itertools import islice
        with open(fname, "w") as myfile:
                myfile.write("Python Exercises\n")
                myfile.write("Java Exercises")
        txt = open(fname)
        print(txt.read())
file_read("test.txt")


# 4.Python program to read last n lines of a file
import sys
import os
def file_read_from_tail(fname,lines):
        bufsize = 8192
        fsize = os.stat(fname).st_size
        iter = 0
        with open(fname) as f:
                if bufsize > fsize:
                        bufsize = fsize-1
                        data = []
                        while True:
                                iter +=1
                                f.seek(fsize-bufsize*iter)
                                data.extend(f.readlines())
                                if len(data) >= lines or f.tell() == 0:
                                        print(''.join(data[-lines:]))
                                        break

file_read_from_tail('test.txt',2)


'''5.Python program to read a file line by line and store it into a list.
def file_read(fname):
        with open(fname) as f:
                #Content_list is the list that contains the read lines.     
                content_list = f.readlines()
                print(content_list)

file_read ('test.txt')

'''

'''6.Python program to read a file line by line store it into a variable
def file_read(fname):
        with open (fname, "r") as myfile:
                data=myfile.readlines()
                print(data)
file_read('test.txt')

'''

'''7.python program to find the longest words. 
def longest_word(filename):
    with open(filename, 'r') as infile:
              words = infile.read().split()
    max_len = len(max(words, key=len))
    return [word for word in words if len(word) == max_len]

print(longest_word('test.txt'))
'''

'''8.Python program to count the number of lines in a text file. 
def file_lengthy(fname):
        with open(fname) as f:
                for i, l in enumerate(f):
                        pass
        return i + 1
print("Number of lines in the file: ",file_lengthy("test.txt"))
'''

'''9.Python program to count the frequency of words in a file.
from collections import Counter
def word_count(fname):
        with open(fname) as f:
                return Counter(f.read().split())

print("Number of words in the file :",word_count("test.txt"))
'''

'''10.Python program to get the file size of a plain file.
def file_size(fname):
        import os
        statinfo = os.stat(fname)
        return statinfo.st_size

print("File size in bytes of a plain file: ",file_size("test.txt"))
'''
