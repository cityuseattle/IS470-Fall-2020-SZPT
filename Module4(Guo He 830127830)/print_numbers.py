def numbers(limis):
    i = 0
    numbers = []

    while i < limis:
        numbers.append(i)
        i = i + 1
    return numbers

user_limis = int(input("Give a limis:"))
print(numbers(user_limis))