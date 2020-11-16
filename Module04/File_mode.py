file = open('hello.txt', 'a')
file.write('\nThis is new content I just appended')
file.close()

file = open('hello.txt')
content = file.read()
file.close()
print(content)