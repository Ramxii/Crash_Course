pet_1 = {
    'specie' : 'hamster',
    'owner' : 'marvin',
}

pet_2 = {
    'specie' : 'dog',
    'owner' : 'kayla',
}

pet_3 = {
    'specie' : 'shark',
    'owner' : 'fizz',
}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"{pet['owner'].title()} owns a cute little {pet['specie']}")
