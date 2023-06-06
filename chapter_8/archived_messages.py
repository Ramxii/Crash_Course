messages = ['hey', 'hi', 'whatsup', 'brb', 'lol']
sent_messages = []

print("---Send Messages---")

def send_messages(texts, sent_texts):
    """Prints each text message and moves it to a new list"""
    while texts:
        for text in texts:
            text = texts.pop()
            sent_texts.append(text)
    return

send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)
