class Computer:

    def __init__(self):
        self.__maxprice = 520
    def sell(self):
        print("selling Price: {}".format(self.__maxprice))
    def setMaxPrice(self, price):
        self.__maxprice = price
c = Computer()
c.sell()
#change the price
c.__maxprice = 1099
c.sell()
#using setter function
c.setMaxPrice( 1098)
c.sell()
