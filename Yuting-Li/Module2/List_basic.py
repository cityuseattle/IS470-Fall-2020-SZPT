List1 = ['physics', 'chemistry', 1997, 2000]
List2 = [1, 2, 3, 4, 5, 6, 7 ]

print("List1[0]: ", List1[0] )
print("List2[1:5]: ", List2[1:5] )

print("Value available at index 2 : ")
print(List1[2])
List1[2] = 2001
print("New Value available at index 2 : ")
print(List1[2])

List1.append(2020)
print("New List:" ,List1)

List1.insert(0, 'Python')
print("After inserting: ",List1)