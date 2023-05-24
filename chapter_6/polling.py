poll = ['annie', 'lisa', 'robert', 'kindred', 'darius']
languages = {
    'annie' : 'python',
    'mark' : 'c',
    'robert' : 'pascal',
    'jina' : 'python',
    'stephanie' : 'java',
}

for name in poll:
    if name in languages.keys():
        print(f"{name} has already taken the poll")
    else:
        print(f"{name} you need to take the poll")
