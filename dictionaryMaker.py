"""
Goals:

Create a dictionary of polish words with the following structure (pulling from kaikkiPol.jsonl)

{
    "root_word":{
        "translations":  [{
            "translation":  "translation",
            "tags":         [""]
        }]
        "word_type":        "noun, adv, character, prefix, intj, name, conj, pron, particle, adj"
        "ipa":              "ipa"
        "rhyme_scheme":     "rhyme_scheme"
        "forms": [{
            "form":         
            "tags":         
        }]
    },
}

Exclude any word that are a form of another word
"""

import json

def build_word(exploring):
    built_dict = {}
    
    sounds = find_sounds(exploring)
        
    built_dict["word_type"] =        exploring["pos"]
    built_dict["translations"] =     build_translations(exploring)
    built_dict["ipa"] =              sounds["ipa"]
    built_dict["rhyme_scheme"] =     sounds["rhyme_scheme"]
    built_dict["forms"] =            build_forms(exploring)
    
    return built_dict

def find_sounds(exploring):
    # Return {"ipa": "ipa", "rhyme_scheme": "rhyme_scheme"}
    sounds = {}
    
    if "sounds" in exploring:
        for sound in exploring["sounds"]:
            if "ipa" in sound:
                sounds["ipa"] =          sound["ipa"]
            elif "rhymes" in sound:
                sounds["rhyme_scheme"] = sound["rhymes"]
    
    if "ipa" not in sounds:
        sounds["ipa"] =              "No ipa found"
        
    if "rhyme_scheme" not in sounds:
        sounds["rhyme_scheme"] =     "No rhyme scheme found"
        
    return sounds

def build_translations(exploring):
    translations = []
        
    for sense in exploring["senses"]:
        
        if "links" in sense:
            for link in sense["links"]:
                translation = {"translation": "[]", "tags": []}
                
                translation["translation"] = link[0]
                
                if "tags" in sense:
                    translation["tags"] = sense["tags"]
                else:
                    translation["tags"] = ["No tags found"]
                
                translations.append(translation)
        
    return translations

def build_forms(exploring):
    forms = []
    
    for form in exploring["forms"]:
        if form["form"] != "no-table-tags" and form["form"] != "pl-decl-noun-m-in":
            f = {}
            
            f["form"] = form["form"]
            
            if "tags" in form:
                f["tags"] = form["tags"]
            else:
                f["tags"] = ["No tags found"]
            
            forms.append(f)
    
    return forms
    
def make_dict(input_file, output_file):
    dictionary = {}
    
    with open("dictionariesSource/" + input_file) as f:
        words = f.readlines()
        
    for word in words:
        exploring = json.loads(word)
        
        if "forms" in exploring and exploring["word"] not in dictionary:
            # Ignores duplicate words for now
            dictionary[exploring["word"]] = build_word(exploring)

    with open("dictionariesMade/" + output_file, "w") as f:
        json.dump(dictionary, f, indent=4)
        
    return dictionary
    
make_dict("kaikkiPol.jsonl", "plDict.json")
# make_dict("kaikkiEng.jsonl", "enDict.json")