pizzas = ['peparoni', 'sausage', 'vegetable', 'tuna', 'bellpeppers']

for pizza in pizzas:
    print(f"I like {pizza}.")

print("\nI really like pizza!")

print("\nThe first three items in the list are: ")
for pizza in pizzas[:3]:
    print(pizza)

print("\nThree items from the middle of the list are:")
for pizza in pizzas[1:4]:
    print(pizza)

print("\nThe last three items in the list are:")
for pizza in pizzas[2:]:
    print(pizza)
