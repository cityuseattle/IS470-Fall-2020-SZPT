print("For-Continue")
for letter in 'Python ' :
    if letter == 'h':
        continue
    print ( 'current Letter : ', letter)

print( "\nwhile-Continue")
var = 10
while var > 0:
    var = var -1
    if var == 5:
        continue
    print ( 'current variable value : ', var)
print ("Good bye!")
