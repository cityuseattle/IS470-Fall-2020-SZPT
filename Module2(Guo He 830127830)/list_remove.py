motorcycles = ['pumb', 'nike', 'adidas']
del motorcycles[1]
print(motorcycles)
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a" , first_owned)
#########################################

motorcycles = ['pumb', 'nike', 'adidas', 'newbanlance']
motorcycles.remove('newbanlance')
print(motorcycles)