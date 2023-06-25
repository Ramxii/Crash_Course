class Users:
    def __init__(self, first_name, last_name, country, age):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.age = age
        self.login_attempt = 0
        return
    
    def describe_user(self):
        """Summary of user information"""
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Country: {self.country}")
        print(f"Age: {self.age}")
        return
    
    def greet_user(self):
        """Greets User"""
        whole_name = f"{self.first_name} {self.last_name}"
        print(f"Good day to you {whole_name.title()}")
        return

    def increment_login_attempt(self, amount=1):
        """Increments the amount of login attempts"""
        self.login_attempt += amount
        return

    def reset_login_attempts(self):
        """Resets the value of login attempts"""
        self.login_attempt = 0
        return


ben = Users('ben', 'mathew', 'usa', 14)

print(ben.login_attempt)
ben.increment_login_attempt()
ben.increment_login_attempt()
ben.increment_login_attempt()
ben.increment_login_attempt()
print(ben.login_attempt)
ben.reset_login_attempts()
print(ben.login_attempt)
