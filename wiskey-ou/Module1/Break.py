print("For-Break")
for letter in ' Python ' :
    if letter == 'h':
        break
    print ( 'current Letter : ', letter)

print( "\nwhile-Break")
var = 10
while var > 0:
    print ( 'current variable value : ' , var)
    var = var -1
    if var == 5:
        break
print ("Good bye !")
