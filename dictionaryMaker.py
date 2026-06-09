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
unacceptable_tags = ["inflection-template", "error-unrecognized-form", "dialectal", "rare", "obsolete", "defective", "archaic", "Łowicz", "Lithuania", "dated", "uncommon", "Poznań", "regional", "Lviv", "form-of"]

def build_word(exploring):
    sounds = find_sounds(exploring)
    
    built_dict = {
        "word_type":        exploring["pos"],
        "translations":     build_translations(exploring),
        "ipa":              sounds["ipa"],
        "rhyme_scheme":     sounds["rhyme_scheme"],
        "forms":            build_forms(exploring)
    }
    
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

def is_english(string):
    try:
        string.encode(encoding="utf-8").decode("ascii")
    except UnicodeDecodeError:
        return False
    else:
        return True

def build_translations(exploring):
    translations = []
        
    for sense in exploring["senses"]:
        acceptable = True
        
        trans_listed = []
        
        while acceptable:
            if "tags" in sense:
                for tag in sense["tags"]:
                    if tag in unacceptable_tags:
                        acceptable = False
            else:
                acceptable = False
                
            if "links" not in sense:
                acceptable = False
            break
        
        if acceptable:
            for link in sense["links"]:
                if is_english(link[0]) and link[0] not in trans_listed:
                    translations.append({"translation": link[0], "tags": sense["tags"]})
                    trans_listed.append(link[0])
        
    return translations

def build_forms(exploring):
    forms = []
    
    for form in exploring["forms"]:
        forms_listed = []
        acceptable = True
        
        while acceptable:
            if form["form"] == "no-table-tags":
                acceptable = False
            elif form["form"] == "pl-decl-noun-m-in":
                acceptable = False
            
            if "tags" in form:
                for tag in form["tags"]:
                    if tag in unacceptable_tags:
                        acceptable = False
            else:
                acceptable = False
                
            if form["form"] in forms_listed:
                acceptable = False
            break
        
        if acceptable:
            f = {"form": form["form"], "tags": form["tags"]}
            forms.append(f)
            forms_listed.append(form["form"])
    
    return forms
    
def make_dict(input_file, output_file):
    dictionary = {}
    
    with open("dictionariesSource/" + input_file) as f:
        words = f.readlines()
        
    for word in words:
        exploring = json.loads(word)
        
        if "forms" in exploring and exploring["word"] not in dictionary:
            # Ignores duplicate words for now
            word = build_word(exploring)
            # Remove words with no valid translation
            if word["translations"] != []:
                dictionary[exploring["word"]] = build_word(exploring)

    with open("dictionariesMade/" + output_file, "w") as f:
        json.dump(dictionary, f, indent=4)
        
    return dictionary
    
make_dict("kaikkiPol.jsonl", "plDict.json")
# make_dict("kaikkiEng.jsonl", "enDict.json")