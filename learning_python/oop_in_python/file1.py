class Employee:
    pass


emp_1 = Employee()
emp_2 = Employee()

emp_1.first = "Test"
emp_1.last = "User"
emp_1.email = "Test.User@company.com"
emp_1.pay = 10000

emp_2.first = "Valid"
emp_2.last = "Username"
emp_2.email = "Valid.Username@company.com"
emp_2.pay = 20000

print(emp_1, emp_2)
print(emp_1.email, emp_2.email)

"""
We use classes to avoid repetitions like the above code
"""
