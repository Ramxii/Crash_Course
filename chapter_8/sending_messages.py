messages = ['hey', 'hello', 'whatup', 'brb']
sent_message = []

def send_messages(texts, sent_texts):
    """Prints all messages in a list"""
    while messages:
        current_text = texts.pop() 
        sent_texts.append(current_text)

send_messages(messages, sent_message)

print(messages)
print(sent_message)
