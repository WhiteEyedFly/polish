# Introduction

Recently I've been trying to pick up Polish for my partner so I figured I'd whip up a little tool to help with my revision.

I found a list online of the 3,000 most common English words and a ripped a Polish to English dictionary and coded up a tester in Python TKinter in a couple hours. It gives you a list of Polish words that all translate to the same English word (though they might have different meanings!) and you have to find the right translation within 3 guesses. 

Each incorrect answer it gives you a hint (or it will when I've finished with it).

v1 and v2 will need extra setup we won't go into here and represent older versions of the project
tensorFlow.py uses an advanced tool to get better translation results but that goes against the spirit of this project and thus this code isn't used in the finished app

# Resources:
https://en.wikipedia.org/wiki/Wikipedia:Database_download
https://kaikki.org/

# Set up
Download wikipedia in the language you wish to use and the relevant Kaikki dictionary from the links above

Place these files in the wikipediasUnparsed and dictionariesSource folders as applicable

Run: dictionaryMaker.py, filterWordByType.py and wordCount.py in that order

Then:

sentenceGenerator.py can be ran to generate a random sentence in your target language with a rough English translation

translator.py can be ran to translate a sentence the user feeds in back to english from the chosen language 

app.py can be used as a revision tool

# app.py
app.py allows you to select your difficulty by preselecting for a subset of the total words present in the dictionary when random words or sentences are generated
It also allows you to select between specific word types, all words or basic sentences to revise
Just press run to launch a TKinter app

# test.py
AI generated code produced after the project was over. It has much less support than the rest of the project because I put far less love into it but I wanted to write "Used AI" on a project so