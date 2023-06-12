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

class Admin(Users):
    """Special user 'Admin' creation"""
    def __init__(self, first_name, last_name, country, age):
        super().__init__(first_name, last_name, country, age)
        """Initialising Admin class"""
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        return

    def show_privileges(self):
        """Displays privileges of Admin"""
        print("List of Priveleges: ")
        for privilege in self.privileges:
            print(f"\t{privilege.title()}")

        return
    
    
ben = Users('ben', 'mathew', 'usa', 14)
robert = Admin('rober', 'hayes', 'st. lucia', 45)

robert.show_privileges()
