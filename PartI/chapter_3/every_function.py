languages = ["french", "spanish", "dutch", "nigerian", "english"]

# list function - shows length of string
print(len(languages))

# sorted function - sort list
print(sorted(languages))

# sorted function - sort in reverse
print(sorted(languages, reverse=True))

# sort method - sorts list permanently
languages.sort()
print(languages)

# sort method reverse - sorts list permanently in reverse
languages.sort(reverse=True)
print(languages)


# pop method - removed list item from end of string and use it
removed = languages.pop()
print(removed)
print(languages)

# append method - adds list item to end of list
languages.append("chinese")
print(languages)

# reverse method - reverses a list permanently
languages.reverse()
print(languages)

# insert method - places a list item anywhere in a list
languages.insert(1, "japanese")
print(languages)

# remove method - removes a specific list item
languages.remove("spanish")
print(languages)

# del function - removes a listed item permanently
del languages[0]
print(languages)
