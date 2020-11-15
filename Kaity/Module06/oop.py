# # name of the class normally use CapWords convention
class Employee:
    # class variable shared by all instance
    emp_count = 0

    def __init__(self, first, last, pay):
        # instance variable unique to each instance
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        # whenever new employee is created,add i to emp_count
        Employee.emp_count += 1
    
    def showinfo(self):
        return '{} {}, {}'.format(self.first, self.last, self.email)
    # pass

emp1 = Employee('Elliot', 'Alderson', 7000)
emp2 = Employee('Jean', 'Grey', 8000)

print(emp1.showinfo())
print("Total Employee:", Employee.emp_count)


# print(emp1)
# print(emp2)

# emp1.first = 'Elliot'
# emp1.last = 'Alderson'
# emp1.email  = 'Elliot.Alderson@comany.com'
# emp1.pay = 7000

# emp2.first = 'Jean'
# emp2.last = 'Grey'
# emp2.email  = 'Jean.Grey@comany.com'
# emp2.pay = 8000


