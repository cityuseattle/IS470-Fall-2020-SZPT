class Employee:
    

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '1037281364@qq.com'

emp_first = Employee('NIKE', 'vision',5201314)
emp_second = Employee('newbalance','Adidas',52013141111)