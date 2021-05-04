# 10.Python program to get the file size of a plain file.
import os
def file_size(fname):
        statinfo = os.stat(fname)
        return statinfo.st_size

print("File size in bytes of a plain file :",file_size("test.txt"))