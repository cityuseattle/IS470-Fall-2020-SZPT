print('This program will sum of numbers from 1 to a number you enter.')
print('Please ENTER A ENDING NUMBER: ')
num = int(input())
total = 0

while num >= 1:
    total += num
    num -= 1

print('The sum is: ' + str(total))