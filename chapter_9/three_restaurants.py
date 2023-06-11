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

bbq = Restaurant('Hot Pork', 'BBQ')
cafe = Restaurant('Tea Time', 'Coffe')
chinese = Restaurant('Xin Woo', 'Takeout')

# BBQ Restaurant
print(bbq.name)
print(bbq.cuisine_type)
bbq.describe_restaurant()
bbq.open_restaurant()
print("\n")
# Cafe Restaurant
print(cafe.name)
print(cafe.cuisine_type)
cafe.describe_restaurant()
cafe.open_restaurant()
print("\n")
# Chinese Restaurant
print(chinese.name)
print(chinese.cuisine_type)
chinese.describe_restaurant()
chinese.open_restaurant()
print("\n")

