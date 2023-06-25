class Restaurant:
    def __init__(self, name, cuisine_type):
        """Restaurant instance"""
        self.name = name
        self.cuisine_type = cuisine_type
        return        

    def describe_restaurant(self):
        """Prints out name and cuisine_type"""
        print(f"Restaurant Name: {self.name}")
        print(f"Restaurant Cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        """Opens the Restaurant"""
        print("The Restaurant is open")
