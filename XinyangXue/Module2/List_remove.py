motorcycles = ['honda', 'yamha', 'suzuki']
del motorcycles[1]
print(motorcycles)
#pop
motorcycles = ['honda', 'yamha', 'suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a" , first_owned)
#remove
motorcycles = ['honda', 'yamha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles)