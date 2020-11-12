dict = {"Name":"abc","Age":7}
print("Name:",dict["Name"],"\n","Age:",dict["Age"])

dict["Age"]=20
print("Updated Age :",dict["Age"])

dict["Phone_no"]=123456789

del dict["Phone_no"]
print("After deleting phone_no:",dict)

first = ["cats","dogs",55]
second = ["dogs",55,"cats"]
print(first==second)

first_dict = {"name":"aaa","species":"human","age":20}
second_dict = {"species":"human","age":20,"name":"aaa"}
print(first_dict==second_dict)

