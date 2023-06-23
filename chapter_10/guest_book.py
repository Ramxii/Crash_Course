from pathlib import Path

path = Path('guest_book.txt')

names_list = ''

while True:
    name = input("What's your name?: ")

    if name == 'End':
        break

    names_list += name + '\n'
    
path.write_text(names_list)
