class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

    def fullname(self):
        return "{} {}".format(self.first, self.last)


emp_1 = Employee("Test", "User", 10000)
emp_2 = Employee("Valid", "Username", 20000)

print(emp_1, emp_2)

print(emp_1.email, emp_2.email)
print(emp_1.fullname(), emp_2.fullname())

print(Employee.fullname(emp_1))     # alternative
