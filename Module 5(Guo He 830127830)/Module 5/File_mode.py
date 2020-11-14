file = open('hello.txt', 'a')
file.write('\nThie is new content I appended')
file.close()


new_file = open('world.txt', 'w')
new_file.write('\nThie is new file')
new_file.close()


file = open('hello.txt')
content = file.read()
file.close()
print(content)
