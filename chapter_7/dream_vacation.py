poll = {}
poll_active = True
while poll_active:
    name = input("\nWhat is your name?: ")
    vacation = input("Where would you like to visit?: ")
    poll[name] = vacation

    answer =  input("\nWould you like to continue? 'no' to quit: ")

    if answer == 'no':
        poll_active = False

print("\n--- Results ---")
for name, vacation in poll.items():
    print(f"{name.title()} would love to visit {vacation.title()}.")
