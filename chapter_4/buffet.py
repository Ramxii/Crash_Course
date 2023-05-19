foods = ['cheeseburger', 'wings', 'salad', 'breadfruit', 'rice'] 

print("The restaurant offers: ")
for food in foods:
    print(food)

foods[0] = 'burger'
foods[1] = 'nutmeg'

print("The restaurant offers: ")
for food in foods:
    print(food)

