class Employee:
   #class variable shared by all instance
   emp_count = 0

   def __init__(self, first, last, pay):
       # instance variable unqiue to each instance
       self.first = first
       self.last = last
       self.pay = pay
       self.email = first + '.' + last + '@acompany.com'
       #whenever new employee is created, add 1 to emp_count
       Employee.emp_count += 1
    
def showinfo(self):
    return '{} {}, {}'.format(self.first, self.last, self.email)

emp1 = Employee('Elliot', 'Alderson', 7000)
emp2 = Employee('Jean', 'Grey', 8000)

print("Total Employee", Employee.emp_count)
print(emp1.showinfo())