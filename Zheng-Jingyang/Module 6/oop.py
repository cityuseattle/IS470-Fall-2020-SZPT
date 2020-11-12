class Employee:
    pass
    emp_count = 0
emp1 = Employee()
emp2 = Employee()
print(emp1)
print(emp2)

emp1.first = 'Jean'
emp2.last = 'Grey'
emp2.email = 'Jeam.Grey@company.com'
emp2.pay = 8000



    def __init__(self, first,last,pay):
       self.first = first
       self.last = last
       self.pay = pay
       self.email = first + '.' + last + '@company.com'

       Employee.emp_count += 1
    
    def showinfo(self):
        return '{} {}, {}'.format(self.first, self.last, self.email) 
emp1 = Employee('Elliot','Alderson',7000)
emp2 = Employee('Jean','Grey',8000)

print(emp1.showinfo())
print("Total Employee:", Employee.emp_count)
