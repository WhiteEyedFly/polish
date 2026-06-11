import json
import random
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

with open("dictionariesMade/plDict.json") as f:
    dictionary = json.load(f)
    
def checker():
    # Guess 1: Starts with "xy"
    # Guess 2: Rhymes with "word"
    global answers, toTranslate, blank, point, incCounter
    
    if entry.get() in answers:
        cv = point.get()
        point.set(cv + 1)
        resp.set("Correct!")
        
        pair = chooseNewWord()
        answers = pair[0]
        toTranslate.set(pair[1])
    else:
        resp.set("Incorrect! Try again")
        incCounter += 1
    blank.set("")
    
    if incCounter > 2:
        resp.set("3 strikes, you're out. '" + toTranslate.get() + "' translates to '" + str(answers) + "'! Let's try something else")
        
        pair = chooseNewWord()
        answers = pair[0]
        toTranslate.set(pair[1])
        
        incCounter = 0

def chooseNewWord():
    pair = random.choice(list(dictionary.items()))
    print(pair)
    toTranslate = pair[0]
    answers = []
    
    for translation in pair[1]["translations"]:
        answers.append(translation["translation"])
    
    return [answers, toTranslate]

def main():
    # Run
    window.mainloop()
    
# Make window
window = ttk.Window(themename="journal")
window.title("Translate the below")
window.geometry("600x450")

# Initialise variables
pair = chooseNewWord()
answers = pair[0]
toTranslate = tk.StringVar()
blank = tk.StringVar()
toTranslate.set(pair[1])
blank.set("")
incCounter = 0
    
# Super structure
main_container = ttk.Frame(master = window)
game_container = ttk.Frame(master = main_container)
options_container = ttk.Frame(master = main_container)

# Options
# Combobox creation
word_type_var = tk.StringVar()
word_type_label = ttk.Label(master = options_container, text = "Select the word type you want to study:")
word_type_box = ttk.Combobox(master = options_container, width = 27, textvariable = word_type_var)

# Adding combobox drop down list
word_type_box['values'] = ('All',
                            'Adjectives', 
                            'Adverbs',
                            'Conjugations',
                            'Interjections',
                            'Names',
                            'Nouns',
                            'Prepositions',
                            'Pronouns',
                            'Verbs')

#word_type_box.grid(column = 1, row = 5)
#word_type_box.current()

# Header
label = ttk.Label(master = game_container, text = "Word to translate:")
word = ttk.Label(master = game_container, textvariable = toTranslate)
resp = tk.StringVar()
point = tk.IntVar()

# Input section
entry_container = ttk.Frame(master = game_container)
entry = ttk.Entry(master = entry_container, textvariable = blank)
button = ttk.Button(master = entry_container, text = "Submit", command = checker)

# Output section
output_container = ttk.Frame(master = game_container)
pointer = ttk.Label(master = output_container, text = "Points: ")
points = ttk.Label(master = output_container, textvariable = point)
response = ttk.Label(master = game_container, textvariable = resp, wraplength=250, justify="center")

# Packing
main_container.pack()
game_container.pack(side = "left", padx = 10)
options_container.pack(side = "left")
# Game
label.pack()
word.pack()
entry_container.pack(pady = 10)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
output_container.pack(pady = 10)
pointer.pack(side = "left")
points.pack(side = "left")
response.pack()
# Options
word_type_label.pack(pady = 10)
word_type_box.pack()

main()

# Remove surnames and first names
# Make a difficulty slider
# Make the word type selector work
# Make a sentence selector
# Make a sentence type selector
# Make a declension tester
# Make a translator
# Write the README
# Package the big files
# Post to git
# Choose next project