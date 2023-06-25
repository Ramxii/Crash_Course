a = input("First Number: ")
b = input("Second Number: ")

try:
    total = int(a) + int(b)
except ValueError:
    print("You can't add anything that isn't a number!")
else:
    print(total)
