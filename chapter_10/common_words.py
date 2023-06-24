from pathlib import Path

def word_checker(book, text):
    """Recieves a book and returns the number of times a text is mentioned"""
    path = Path(book)
    lines = path.read_text().splitlines()
    count = 0
    
    for line in lines:
        count += line.lower().count(' ' + text + ' ')
    
    return print(count)

word_checker('alice_in_wonderland.txt', 'foot')
