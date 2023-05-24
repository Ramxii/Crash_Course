favorite_places = {
    'melissa' : ['castries', 'soufriere'],
    'john' : ['anse - la - raye', 'vieux fort'],
    'benson' : ['micoud']
}

for person, places in favorite_places.items():
    print(f"\n{person} favorite place/s is: ")
    for place in places:
        print(f"{place}")
