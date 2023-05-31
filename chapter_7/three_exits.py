'''
prompt = 'What is your age? '
prompt += 'Use 0 to quit: '
active = True
while active:
    age = input(prompt)
    age = int(age)
    if age == 0:
        print('quit')
        active = False
    elif age < 3:
        print("They can enter for free")
    elif age < 12:
        print("The fee is $10")
    else:
        print("Fee is $15")
'''
'''
prompt = 'What is your age? '
prompt += 'Use 0 to quit: '
while True:
    age = input(prompt)
    age = int(age)
    if age == 0:
        print('quit')
        break
    elif age < 3:
        print("They can enter for free")
    elif age < 12:
        print("The fee is $10")
    else:
        print("Fee is $15")
'''

prompt = 'What is your age? '
prompt += 'Use 0 to quit: '
age = ''
while age != 0:
    age = input(prompt)
    age = int(age)
    if age == 0:
        print('quit')
    elif age < 3:
        print("They can enter for free")
    elif age < 12:
        print("The fee is $10")
    else:
        print("Fee is $15")
