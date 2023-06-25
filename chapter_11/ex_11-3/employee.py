class Employee:
    """Stores first, last names and anual salary"""
    def __init__(self, first, last, salary):
        """ Takes in first, last name and salary"""
        self.first = first
        self.last = last
        self.salary = salary

    def give_raise(self, amount=5000):
        """Adds raise to salary"""
        self.salary += amount
        return self.salary

