class Employee:

    raise_amount = 1.04
    num_of_emps = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

        Employee.num_of_emps += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee("Test", "User", 10000)
emp_2 = Employee("Valid", "Username", 20000)

print(emp_1.raise_amount)
print(Employee.raise_amount)

# print the namespace of an object
print(emp_1.__dict__)
print(Employee.__dict__)

Employee.raise_amount = 1.05
print(Employee.raise_amount)

emp_1.raise_amount = 1.06
print(emp_1.raise_amount)
print(emp_1.__dict__)

print("Number of employees:", Employee.num_of_emps)
