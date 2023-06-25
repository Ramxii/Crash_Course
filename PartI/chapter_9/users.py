class Users:
    def __init__(self, first_name, last_name, country, age):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.age = age
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

ben = Users('ben', 'mathew', 'usa', 14)
tyler = Users('tyler', 'rich', 'barbados', 22)
lisa = Users('lisa', 'montgemery', 'london', 45)

# Ben information
ben.greet_user()
ben.describe_user()
print('\n')
# Tyler information
tyler.greet_user()
tyler.describe_user()
print('\n')
# Lisa information
lisa.greet_user()
lisa.describe_user()
print('\n')
