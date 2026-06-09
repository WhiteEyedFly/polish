import json

types = ["noun", "character", "name", "prefix", "pron", "conj", "adj", "suffix", "phrase", "particle", "verb", 
         "intj", "num", "adv", "prep", "det", "punct", "interfix", "proverb"]

sourceDict = {
    "english": "dictionariesMade/enDict.json",
    "polish": "dictionariesMade/plDict.json"
}

def open_dict(input_file):
    with open(input_file) as f:
        return json.load(f)

def find_word_types(input_file):
    word_types = []
    
    dictionary = open_dict(input_file)

    for word in dictionary.keys():
        if dictionary[word]["word_type"] not in word_types:
            word_types.append(dictionary[word]["word_type"])
    
    return word_types

def print_words_by_type(input_file, type):
    dictionary = open_dict(input_file)
    
    for word in dictionary.keys():
        if dictionary[word]["word_type"] == type:
            print(word, dictionary[word]["translations"][0])
            print(" ")

def remove_ing(dictionary):
    for word in dictionary:
        for form in dictionary[word]["forms"]:
            acceptable = True
            forms_list = []
            
            while acceptable:
                if dictionary[word]["word_type"] != "verb" and word[-3:] == "ing":
                    acceptable = False
                elif dictionary[word]["word_type"] != "verb" and word[-3:] == "ing":
                    acceptable = False 
                break
                
            if acceptable:
                forms_list.append(form)
        
        if forms_list != []:
            dictionary[word]["forms"] = forms_list
    
    return dictionary

def filter_by_type(language):
    input_file = sourceDict[language]
    dictionary = open_dict(input_file)
    
    important_types = [["adj" , "adjectives", {}], 
                       ["adv" , "adverbs", {}], 
                       ["conj", "conjugations", {}], 
                       ["intj", "interjections", {}], 
                       ["name", "names", {}], 
                       ["noun", "nouns", {}], 
                       ["prep", "prepositions", {}], 
                       ["pron", "pronouns", {}], 
                       ["verb", "verbs", {}]]
    i_types = ["adj", "adv", "conj", "intj", "name", "noun", "prep", "pron", "verb"]
    
    # Filter
    for word in dictionary.keys():
        acceptable = True
        
        while acceptable:
            # Ignore unimportant types
            if dictionary[word]["word_type"] not in i_types:
                acceptable = False
                
            # Ensure entries to names are capitalised and entries to others are not
            if dictionary[word]["word_type"] != "name" and word[0].isupper():
                acceptable = False
            elif dictionary[word]["word_type"] == "name" and not word[0].isupper():
                acceptable = False
                
            break
        
        if acceptable:
            important_types[i_types.index(dictionary[word]["word_type"])][2][word] = dictionary[word]
    
    for entry in range(len(important_types) - 1):
        important_types[entry][2] = remove_ing(important_types[entry][2])
    
    # Post to .jsons
    for entry in range(len(important_types)):
        with open(language + "WordsByType/" + important_types[entry][1] + ".json", "w") as f:
            json.dump(important_types[entry][2], f, indent=4)

# print(find_word_types("dictionariesMade/plDict.json"))
# print_words_by_type("dictionariesMade/plDict.json", "prep")
filter_by_type("polish")
# Word types are: noun, character, name, prefix, pron, conj, adj, suffix, phrase, particle, verb, intj, num, adv, prep, det, punct, interfix, proverb