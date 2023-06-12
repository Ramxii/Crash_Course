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
        return

    def open_restaurant(self):
        """Opens the Restaurant"""
        print("The Restaurant is open")
        return

class IceCreamStand(Restaurant):
    """Represents aspects of a Restaurant, specific to Ice-cream Stands """
    def __init__(self, name, cuisine_type):
        """Initialise attributes of the parent class Restaurant"""
        super().__init__(name, cuisine_type)
        self.flavors = ['strawberry', 'vanilla', 'chocolate']
        return

    def list_flavors(self):
        """List the different kinds of flavors"""
        print(f"{self.name.title()} Flavors: ")
        for flavor in self.flavors:
            print(f"\t{flavor}")

        return

choc_ice = IceCreamStand('Choc Ice', 'Ice-Cream')
choc_ice.list_flavors()
