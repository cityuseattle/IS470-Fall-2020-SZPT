def order (number, *lists):
    print(f"\nNumber of dishes: {number}, The dishes are:")
    for list in lists:
        print(f"-{list}")

import order_module

order_module.order(1,"Pizza")
order_module.order(3,"Soup","Pasta","Pizza")