from random import choice

lottery = ( 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b', 'c', 'd', 'e' )

def lottery_system():
    winning_tickets = []
    while len(winning_tickets) < 4:
        # Pick a ticket
        ticket = choice(lottery)

        # Append the ticket if it hasn't been selected 
        if ticket not in winning_tickets:
            winning_tickets.append(ticket)
    
    return winning_tickets



# probability of winning the lottery with my ticket
probability = 0
winner = False

while winner != True:
    my_ticket = lottery_system()
    winning_tickets = lottery_system()

    if my_ticket == winning_tickets:
        winner = True
        print(f"Your tickets are {my_ticket}")
        print(f"The winningtickets are {winning_tickets}")

    probability = probability + 1

print(f"It took you {probability} tries to win!")


