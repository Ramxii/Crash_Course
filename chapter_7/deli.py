sandwich_orders = ['turkey', 'ham', 'bacon', 'chicken', 'sausage']
finished_sandwiches = []

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)

    print(f"Your {sandwich} sandwich has been done.")
