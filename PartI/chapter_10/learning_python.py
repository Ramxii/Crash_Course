from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text().rstrip()

# Reading the entire file
print("\tReading the entire file: ")
print(contents)

# Reading line by line
lines = contents.splitlines()
line_list = []

print("\n\tReading Line by Line: ")
for line in lines:
    line_list.append(line)
    print(line)
