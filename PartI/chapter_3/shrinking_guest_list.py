guests = ["Al Paccino", "Dave Chappelle", "Marcus Garvey"]

guests.insert(0, "Angelina Jolie") 
guests.insert(3, "Linus Tovalds") 
guests.append("Kendrick Llamar") 

print(f"{guests[0]}, you are invited to dinner")
print(f"{guests[1]}, you are invited to dinner")
print(f"{guests[2]}, you are invited to dinner")
print(f"{guests[3]}, you are invited to dinner")
print(f"{guests[4]}, you are invited to dinner")
print(f"{guests[5]}, you are invited to dinner")

print("\nI'm sorry but I can only invite two persons")

uninvited = guests.pop()
print(f"I'm sorry {uninvited} but you aren't invited anymore")

uninvited = guests.pop()
print(f"I'm sorry {uninvited} but you aren't invited anymore")

uninvited = guests.pop()
print(f"I'm sorry {uninvited} but you aren't invited anymore")

uninvited = guests.pop()
print(f"I'm sorry {uninvited} but you aren't invited anymore")

print("\n")

print(f"Good evening {guests[0]}, you're still invited to the dinner")
print(f"Good evening {guests[1]}, you're still invited to the dinner")

del guests[0]
del guests[0]

print(guests)
