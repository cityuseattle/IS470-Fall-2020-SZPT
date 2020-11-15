class Employee:
    pass

emp1 = Employee()
emp2 = Employee()
print(emp1)
print(emp2)
emp_count = 0


#whenever new employee is created, add 1 to emp_count
Employee.emp_count += 1

def showinfo(self):
    return '{} {}, {}'.format(self.first, self.last, self.email)



print(emp1.showinfo())
print("Total Employee:", Employee.emp_count)
