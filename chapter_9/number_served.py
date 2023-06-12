class Restaurant:
    def __init__(self, name, cuisine_type):
        """Restaurant instance"""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        return        

    def describe_restaurant(self):
        """Prints out name and cuisine_type"""
        print(f"Restaurant Name: {self.name}")
        print(f"Restaurant Cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        """Opens the Restaurant"""
        print("The Restaurant is open")
        return

    def show_number_served(self):
        """Reads the number served"""
        print(f"Number Served: {self.number_served}")
        return

    def set_number_served(self, served):
        """Sets the number for served patrons"""
        self.number_served = served
        return

    def increment_number_served(self, inc_served):
        """Increments on the number of served patrons"""
        self.number_served += inc_served
        return
    

restaurant = Restaurant('Chef Ablaze', 'BBQ')
restaurant.show_number_served()
restaurant.number_served = 30
restaurant.show_number_served()

restaurant.set_number_served(32)
restaurant.show_number_served()

restaurant.increment_number_served(55)
restaurant.show_number_served()
