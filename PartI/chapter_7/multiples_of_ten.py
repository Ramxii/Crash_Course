prompt = input("Give me a number: ")
prompt = int(prompt)

if prompt % 10 == 0:
    print(f"{prompt} is a multiple of 10")
else:
    print(f"{prompt} is not a multile of 10")
