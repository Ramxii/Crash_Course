from pathlib import Path

file_names = ['cats.txt', 'dogs.txt']

for file in file_names:
    try:
        path = Path(file)
    except FileNotFoundError:
        print("Error 404: No file found")
    else:
        contents = path.read_text().rstrip()
        print(contents)
