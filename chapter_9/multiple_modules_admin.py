from multiple_modules_user import Users
from multiple_modules_privileges import Privileges

class Admin(Users):
    """Special user 'Admin' creation"""
    def __init__(self, first_name, last_name, country, age):
        super().__init__(first_name, last_name, country, age)
        """Initialising Admin class"""
        self.whole_name = f"{self.first_name} {self.last_name}"
        return
    
    privileges = Privileges()

