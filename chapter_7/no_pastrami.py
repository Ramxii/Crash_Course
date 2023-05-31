sandwich_orders = ['pastrami', 'turkey', 'ham', 'bacon', 'pastrami', 'chicken', 'sausage', 'pastrami']
finished_sandwiches = []
print("The deli has ran out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches.append(sandwich)

    print(f"Your {sandwich} sandwich has been done.")
