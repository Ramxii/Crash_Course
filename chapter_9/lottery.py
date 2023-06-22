from random import choice

lottery = ( 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e' )
winning_tickets = []

print("Your winning lottery tickets are: ")
for i in range(4):
    winning_tickets.append(choice(lottery))

print(winning_tickets)

print("Your winning tickets are: ")
for ticket in winning_tickets:
    print(f"\t{ticket}")
