prompt = 'What is your age?: '
active = True
while active:
    age = input(prompt)
    if int(age) < 3:
        print("They can enter for free")
    elif int(age) < 12:
        print("The fee is $10")
    else:
        print("Fee is $15")
