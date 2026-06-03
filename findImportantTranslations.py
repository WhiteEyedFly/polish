import json

# Important Words - English
iWE = [line for line in open("threeThousand.txt", "r")]
# All Polish words and translations
polishWords = [line for line in open("wordsListBetter.txt", "r")]
polishDict = {}

# Remove \n's
for word in range(len(iWE)):
    iWE[word] = iWE[word][:len(iWE[word])-1]

for word in range(len(polishWords)):
    polishWords[word] = polishWords[word][:len(polishWords[word])-1]

# Split polishWords on -
polishWordsOnly = []
for word in range(len(polishWords)):
    i = polishWords[word].index(" - ")
    translation = polishWords[word][:i]
    polishWord = polishWords[word][i+2:]
    if translation in iWE:
        polishDict[polishWords[word][:i]] = polishWords[word][i+2:]

with open("polishDict.json", "w") as f:
    json.dump(polishDict, f, indent=4)
    

