messages = ('hey', 'hello', 'whatup', 'brb')

def show_message(texts):
    """Prints all messages in a list"""
    for text in texts:
        print(f"{text}")

show_message(messages)
