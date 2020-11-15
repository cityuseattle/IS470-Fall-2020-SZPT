try:
    fh = open("testfile","r")
    fh.write("This is my test file fpr exception handling!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("written content in the file successfully")
    fh.close()