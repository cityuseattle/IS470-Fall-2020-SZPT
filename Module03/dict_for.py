alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}

alien = [alien_0,alien_1]

#Accessing key,value
for i in alien:
    for key,value in i.items():
        print("KEY: ", key, "\t" , "VALUE :",value)