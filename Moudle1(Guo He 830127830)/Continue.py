print("For-Continue")
for letter in 'Python':
    if letter == 'h':
        continue
    print ('Curren LETTER :', letter)

print("\nWhile-Break")
var = 10
while var > 0:
    var = var -1
    if var == 5:
        continue
    print('Current variable value :',var)
    print("Good bye!")