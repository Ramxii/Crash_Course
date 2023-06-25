person_1 = {
    'firstname' : 'Lisa',
    'last_name' : 'Falmor',
    'age' : 13,
    'city' : 'England',
}
person_2 = {
    'firstname' : 'Xion',
    'last_name' : 'Cheng',
    'age' : 25,
    'city' : 'Beijing',
}
person_3 = {
    'firstname' : 'Mical',
    'last_name' : 'Jona',
    'age' : 43,
    'city' : 'Los Angeles',
}

people = [person_1, person_2, person_3]

for person in people:
    print(f"\nName: {person['firstname']} {person['last_name']}")
    print(f"Age: {person['age']}")
    print(f"Residence: {person['city']}")
