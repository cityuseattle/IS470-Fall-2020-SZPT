class Employee:

    emp_count = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + 'acompany.com'

        Employee.emp_count += 1

    def showinfo(self):
        return '{} {}, {}'.format(self.first,self.last,self.email)

emp_first = Employee('NIKE', 'vision', 5201314)
emp_second = Employee('newbalance', 'morning', 52013141111)

print(emp_first.showinfo())
print("Total Employee: ", Employee.emp_count)