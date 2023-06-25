prompt = input("How many people are in your dinner group?: ")
prompt = int(prompt)

if prompt > 8:
    print("They'll have to wait for a table.")
else:
    print("Your table is ready.")
