# Clear wordList
with open("wordList.txt", "w") as f:
    f.write("")

# Validate word list
with open("words.txt") as f:
    words = str(f.read()).split()

for word in range(len(words)):
    equalPos = words[word].index("=")
    words[word] = words[word][:equalPos]

with open("wordList.txt", "a") as f:
    for word in words:
        f.write(word)
        f.write("\n")

