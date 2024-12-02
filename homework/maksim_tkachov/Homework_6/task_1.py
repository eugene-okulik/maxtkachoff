text = 'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, dignissim vitae libero'
words = text.split()
updated_words = []
for word in words:
    if word[-1] in ',.':
        updated_words.append(word[:-1] + 'ing' + word[-1])
    else:
        updated_words.append(word + 'ing')
result = ' '.join(updated_words)
print(result)
