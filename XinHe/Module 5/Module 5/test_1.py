try:
    fh = open("testfile","w")
    fh.write("This is my test file")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("written content in the file successfully")
    fh.close()