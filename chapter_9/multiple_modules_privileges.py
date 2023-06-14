class Privileges():
    """docstring for Priveleges."""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        return

    def show_privileges(self):
        """Displays privileges"""
        for privilege in self.privileges:
            print(f"\t{privilege.title()}")

        return

