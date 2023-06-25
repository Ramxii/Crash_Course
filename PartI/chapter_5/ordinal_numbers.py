ordinal = list(range(1, 10))

for number in ordinal:
    if number is 1:
        print(f"{number}st")
    elif number is 2:
        print(f"{number}nd")
    elif number is 3:
        print(f"{number}rd")
    else:
        print(f"{number}th")
