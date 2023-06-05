messages = ['hey', 'hello', 'whatup', 'brb']
sent_message = []

def show_message(texts, sent_texts):
    """Prints all messages in a list"""
    print("\n---Sending Messages---")
    while messages:
        current_text = texts.pop() 
        print(f"Sending: {current_text}")
        sent_texts.append(current_text)

    print("\n---Sent Messages---")
    for text in sent_texts:
        """Prints all sent texts"""
        print(f"Sent: {text}")


show_message(messages, sent_message)
