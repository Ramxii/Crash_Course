from pathlib import Path
import json

path = Path("user_info.json")

def takes_user():
    """Prompts for username, age, country"""
    name = input("Username: ")
    age = input("Age: ")
    country = input("Country: ")
    print(f"Till next time {name}!")

    user = {
        'name' : name,
        'age' : age,
        'country' : country,
    }

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
    return user_info['name']

def check_user():
    """Verifies the current user"""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        answer = input(f"Are you {user_info['name']}?\n('y' or 'n'): ")
        if answer == 'y' :
            displays_user()
        else:
            takes_user()
    else:
        takes_user()
    
    return

check_user()
