def number(limit):
    i = 0
    number = []

    while i < limit:
        number.append(i)
        i = i + 1
    return number
user_limit = int(input("Give a limit: "))
print(numbers(user_limit))