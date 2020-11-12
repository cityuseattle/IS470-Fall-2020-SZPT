#####################
dict = {'NAME':'abc','Age':7}
print ("Name : ", dict['NAME'] ,"\n" , "Age :",dict['Age'])

#######################
dict['Age'] = 20
print("Updated Age :", dict['Age'])

##################
dict['PHONE_NUMBER'] = 111111111
print("AFTER ADDING THE NEW PAIR :", dict)

################
del dict['PHONE_NUMBER']
print("AFTER DELETING PHONE_NUMBER :", dict)