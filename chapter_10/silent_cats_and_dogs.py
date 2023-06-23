from pathlib import Path

file_names = ['cats.txt', 'dogs.txt']

for file in file_names:
    try:
        path = Path(file)
    except FileNotFoundError:
        pass
    else:
        contents = path.read_text().rstrip()
        print(contents)
