rivers = {
    'egypt' : 'nile',
    'america' : 'mississippi',
    'south america' : 'amazon',
    'eaurope' : 'danube',
    'asia' : 'indus',
}

for country, river in rivers.items():
    print(f"The {river.title()} River runs through {country.title()}")

print('\n')
for river in rivers.values():
    print(f"The {river.title()} River is one of the largest in the world.")

print('\n')
for country in rivers.keys():
    print(f"{country.title()} houses one of the largest rivers.")
