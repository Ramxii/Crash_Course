prompt = ("What pizza toppings would you like?: ")
active = True

while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)
