def order (number, *lists):
    print(f"\nNumber of dishes: {number}, The dishes age:")
    for list in lists:
        print(f"-{list}")