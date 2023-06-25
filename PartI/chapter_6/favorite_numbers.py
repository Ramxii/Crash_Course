favorite_numbers = {
    'joana' : [23 , 44] ,
    'mark' : [10 , 56, 52] ,
    'lisa' : [3, 92, 144] ,
   'melani' : [5, 3, 1] ,
    'tom' : [78, 63] ,
} 

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} is:")
    for number in numbers:
        print(f"\t{number}")
