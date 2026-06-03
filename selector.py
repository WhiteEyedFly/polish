import json
import random
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk

with open("polishDict.json") as f:
    dictionary = json.load(f)
    
def checker():
    global answer, toTranslate, blank, point, incCounter
    print(incCounter)
    
    if entry.get() == answer:
        cv = point.get()
        point.set(cv + 1)
        resp.set("Correct!")
        
        pair = chooseNewWord()
        answer = pair[0]
        toTranslate.set(pair[1])
    else:
        resp.set("Incorrect! Try again")
        incCounter += 1
    blank.set("")
    
    if incCounter > 2:
        resp.set("3 strikes, you're out. '" + toTranslate.get() + "' translates to '" + answer + "'! Let's try something else")
        
        pair = chooseNewWord()
        answer = pair[0]
        toTranslate.set(pair[1])
        
        incCounter = 0

def chooseNewWord():
    pair = random.choice(list(dictionary.items()))
    answer = pair[0]
    toTranslate = random.choice(pair[1])
    
    return [answer, toTranslate]

def main():
    # Run
    window.mainloop()
    
# Make window
window = ttk.Window(themename="journal")
window.title("Translate the below")
window.geometry("400x250")

# Initialise variables
pair = chooseNewWord()
answer = pair[0]
toTranslate = tk.StringVar()
blank = tk.StringVar()
toTranslate.set(pair[1])
blank.set("")
incCounter = 0
    
# Header
label = ttk.Label(master = window, text = "Word to translate:")
word = ttk.Label(master = window, textvariable = toTranslate)
resp = tk.StringVar()
point = tk.IntVar()

# Input section
entry_container = ttk.Frame(master = window)
entry = ttk.Entry(master = entry_container, textvariable = blank)
button = ttk.Button(master = entry_container, text = "Submit", command = checker)

# Output section
output_container = ttk.Frame(master = window)
pointer = ttk.Label(master = output_container, text = "Points: ")
points = ttk.Label(master = output_container, textvariable = point)
response = ttk.Label(master = window, textvariable = resp, wraplength=250, justify="center")

# Packing
label.pack()
word.pack()
entry_container.pack(pady = 10)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
output_container.pack(pady = 10)
pointer.pack(side = "left")
points.pack(side = "left")
response.pack()

main()