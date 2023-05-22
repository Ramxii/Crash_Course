current_users = ['daniel', 'kayla', 'marvin', 'felise', 'joanna', 'admin']
new_users = ['john', 'tyler', 'MARVIN', 'kindred', 'miss fortune']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user.lower()} has already signed in. Enter a new username: ")
    else:
        print(f"Welcome {new_user}")
