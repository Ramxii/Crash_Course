# favorite numbers program extended
favorite_numbers = {
    'joana' : [23 , 44],
    'mark' : [10 , 56, 52],
    'lisa' : [3, 92, 144],
    'melani' : [5, 3, 1],
    'tom' : [78, 63],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s numbers are:")
    for number in numbers:
        if number <= 10:
            print(f"\t{number} - That's a really small number...")
        elif number <= 50:
            print(f"\t{number} - That's a great number.")
        elif number:
            print(f"\t{number} - Wow! You're really going big!")
