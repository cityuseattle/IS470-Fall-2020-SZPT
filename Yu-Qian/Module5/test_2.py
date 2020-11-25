try:
    fh=open("testfile.txt","r")
    fh.write("This is my test file for exception handing!!")
except IOError:
    print("Error: can\'t find file or read data")
else:
    print("Written content in the file successfully")
    