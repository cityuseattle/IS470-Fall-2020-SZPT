#del
motorcycles = ['honda','yamaha','suzuki']
del motorcycles[1]
#pop
motorcycles = ['honda','yamaha','suzuki']
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
first_owned = motorcycles.pop(0)
print("The first motorcycle I owmed was a ",first_owned)

#remove
motorcycles = ['honda','yamaha','suzuki','ducati']
motorcycles.remove('ducati')
print(motorcycles)
