unsent_messages = ['hey', 'hello', 'whatup', 'brb']
sent_messages = []

def send_messages(texts, sent_texts):
    """Prints all messages in a list"""
    while unsent_messages:
        current_text = texts.pop() 
        sent_texts.append(current_text)

send_messages(unsent_messages[:], sent_messages)

print(unsent_messages)
print(sent_messages)

