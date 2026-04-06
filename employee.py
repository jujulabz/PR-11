class Employee:
    """A class to represent an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Increase salary by default $5000 or a custom amount."""
        self.annual_salary += amount