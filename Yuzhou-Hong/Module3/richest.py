income = {"Alice":9000,
          "Bob":100000,
        "Jeff":20000,
        "Alex":3000000,
        "Je":999998,
        "Stark":99999,
}
highest = max(income,key=income.get)
print("the richest man is",end=" ")
print(highest+" with $ "+ str(income[highest]))