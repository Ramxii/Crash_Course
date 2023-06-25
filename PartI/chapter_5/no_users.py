#user_names = ['daniel', 'kayla', 'marvin', 'felise', 'joanna', 'admin']
user_names = []

if user_names:
    for user in user_names:
        if user == 'admin':
            print("Welcome System Administrator")
        else:
            print(f"Hello {user}, thank you for logging in")
else:    
    print("There's no users in the system")
