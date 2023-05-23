glossary = {
    'Conditional statements' : 'evaluate to true or false.',
    'If statements' : 'runs a block of code based on whether or not a condition is true.',
    'Loops' : 'check a condition and then run a code block. The loop will continue to check and run until a specified condition is reached.',
    'Strings' : 'is a sequence of characters and can contain letters, numbers, symbols and even spaces. It must be enclosed in quotation marks for it to be recognized as a string.',
    'Variable' : 'storing values so that we can reuse them throughout our code or change them, if necessary.',
}

for word, definition in glossary.items():
    print(f"{word}:\n\t{definition}\n")
