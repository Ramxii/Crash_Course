age = 37
person = ''

if age < 2:
    person = 'baby'
elif age <= 4:
    person = 'toddler'
elif age <= 13:
    person = 'kid'
elif age <= 20:
    person = 'teenager'
elif age <= 65:
    person = 'adult'
elif age > 65:
    person = 'elder'

print(f"This person is a/n {person}")
