
class Employee:

    raise_amount = 1.04
    num_of_devs = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + "@company.com"

        Employee.num_of_devs += 1

    def fullname(self):
        return "{} {}".format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


class Developer(Employee):
    pass


dev_1 = Developer("Test", "User", 10000)
dev_2 = Developer("Valid", "Username", 20000)

print(dev_1.email, dev_2.email)

"""
Here two Developer objects were created successfully and we can access the attributes
that were present in Employee class. So when we instantiated the Developer objects, the interpreter
first looked into the Developer class for the __init__ method and it didn't find it so it walked up
the chain of inheritance until it finds what it's looking for. This chain is called the 
"method resolution order".
"""

print(help(Developer))
