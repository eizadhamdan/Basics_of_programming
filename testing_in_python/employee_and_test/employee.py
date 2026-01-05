class Employee:
    """A simple Employee class"""

    raise_amount = 1.05

    def __init__(self, first_name, last_name, salary, position="Fresher"):
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.salary = salary

    @property
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@company.com"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def give_raise(self, amount=None):
        if amount is not None and amount < 0:
            raise ValueError("Raise amount must be positive")
        if amount is not None:
            self.salary += amount
        else:
            self.salary *= self.raise_amount

    def promote(self, new_position, raise_amount):
        self.position = new_position
        self.give_raise(raise_amount)
