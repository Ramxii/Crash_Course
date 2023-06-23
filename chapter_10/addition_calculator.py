def addition():
    """Prompts the user to input two numbers then prints the total"""
    total = 0
    while True:
        a = input("First Number:('q' to quit) ")
        if a == 'q':
            break
         
        b = input("Second Number:('q' to quit) ")
        if a == 'q':
            break
        

        try:
            total += int(a) + int(b)
        except ValueError:
            print("You can't add anything that isn't a number!")
        else:
            print(f"Your total of {a} and {b} is {total}\n")
        
    return total

addition()
