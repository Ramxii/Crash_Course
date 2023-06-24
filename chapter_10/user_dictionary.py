from pathlib import Path
import json

path = Path("user_info.json")

def takes_user():
    """Prompts for username, age, country"""
    user = {}

    user['name'] = input("Username: ")
    user['age'] = input("Age: ")
    user['country'] = input("Country: ")

    contents = json.dumps(user)
    path.write_text(contents)
    return user

def displays_user():
    """Displays user info"""
    contents = path.read_text()
    user_info = json.loads(contents)
    print(f"Good day to you {user_info['name'].title()}.")
    print(f"Must be nice being {user_info['age']}.")
    print(f"Especially when visiting from {user_info['country']}.")

if path.exists():
    displays_user()
else:    
    takes_user()
