cities = {
    'Beijing' : {
        'country' : 'china',
        'polulation' : '21',
        'fact' : 'bathe in milk',
    },
    'New York' : {
        'country' : 'united states of america',
        'polulation' : '10',
        'fact' : 'sacrifices to the sun god',
    },
    'London' : {
        'country' : 'england',
        'polulation' : '8',
        'fact' : 'bats fly in the morning',
    }
}

for city, information in cities.items():
    print(f"\n{city.title()} City:")
    for info, data in information.items():
        print(f"\t{info.title()}: {data.title()}")
