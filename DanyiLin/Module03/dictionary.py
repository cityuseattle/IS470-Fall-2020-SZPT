#Accessing 
dict = {'Name':'abc', 'Age': 7 }
print("NAme : ",dict['Name'],"\n","Age :",dict['Age'])

#updating
dict['Age'] = 20
print("Updated Age :",dict['Age'])


#Adding 
dict['Python_no'] = 123456789
print("After adding the new pair : ", dict)

#Deleting 
del dict['Python_no']
print("After deleting python_no : ", dict)
