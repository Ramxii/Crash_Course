pizzas = ['peparoni', 'sausage', 'vegetable', 'tuna', 'bellpeppers']

friend_pizzas = pizzas[:]

pizzas.append('mushroom')
friend_pizzas.append('anchovee')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\n")

print("My friend favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
