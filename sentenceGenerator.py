import random as rand
import json

plBasicSS = ["Subject", ["Verb"], ["Object", ["Noun"], ""]]

# "Verb" includes adverbs, "Noun" includes adjectives
# Subject adverb verb adjective noun
# Additions: ["Locative", ""], ["Vocative", ""], ["Instrumental", ""], ["Preposition", ""]
# Conjugations: ["Basic", "Conjunction", "Basic"]
# Interjections

# A subject is: a name, an identifier ("the dog"), a pronoun

sourceDict = {
    "english": "dictionariesMade/enDict.json",
    "polish": "dictionariesMade/plDict.json"
}

def with_(language):
    if language == "english":
        return "with"
    elif language == "polish":
        return "z"

def open_dict(input_file):
    with open(input_file) as f:
        return json.load(f)
    
def get_translation(word):
    translation = word["translations"][0]["translation"]
    return translation 

def intj_gen(language):
    # Return a random intj and it's most common translation
    intjs = open_dict(language + "WordsByType/interjections.json")
    
    intj, data = rand.choice(list(intjs.items()))
    translation = get_translation(data)
    
    return [intj, translation]

def chain_gen(language, tense, perfectivitychain_limit, verb=True):
    if verb:
        chainer = open_dict(language + "WordsByType/adverbs.json")
        finisher = open_dict(language + "WordsByType/verbs.json")
    else:
        chainer = open_dict(language + "WordsByType/adjectives.json")
        finisher = open_dict(language + "WordsByType/nouns.json")
    
    chain_len = rand.randint(0, chain_limit)
    
    chain = ""
    t_chain = ""
    
    for n in range(chain_len):
        chainee, chainee_data = rand.choice(list(chainer.items()))
        translation = get_translation(chainee_data)
        
        if n == 0:
            chain = chainee
            t_chain = translation
        else:
            chain = chain + ", " + chainee
            t_chain = t_chain + ", " + translation
    
    finish, finish_data = rand.choice(list(finisher.items()))
    translation = get_translation(finish_data)
    
    if chain_len > 0:
        chain = chain + " " + finish
        t_chain = t_chain + " " + translation
    else:
        chain = finish
        t_chain = translation
    
    return [chain, t_chain]

def subject_gen(language, tense, perfectivity):
    options = ["names", "pronouns", "nouns"]
    chosen_type = options[rand.randint(0, len(options)-1)]
    
    if chosen_type == "names":
        chosen_dict = open_dict(language + "WordsByType/names.json")
        name, data = rand.choice(list(chosen_dict.items()))
        return [name, name]
    elif chosen_type == "pronouns":
        chosen_dict = open_dict(language + "WordsByType/pronouns.json")
        pron, data = rand.choice(list(chosen_dict.items()))
        translation = get_translation(data)
        return [pron, translation]
    else:
        return chain_gen(language, tense, perfectivity, c_lim, verb=False)

def third_gen(language, tense, perfectivity):
    if rand.random() < 0.5:
        return chain_gen(language, tense, perfectivity, c_lim, verb=False)
    else:
        return ["", ""]
    
def extras_gen(language):
    # Additions: ["Locative", ""], ["Vocative", ""], ["Instrumental", ""], ["Preposition", ""]
    # In a place
    # A noun you are speaking to
    # With a thing
    # Preposition comes before locative, times are locative
    
    options = ["Locative", "Vocative", "Instrumental", ""]
    chosen_type = options[rand.randint(0, len(options)-1)]
    
    chain = ""
    t_chain = ""
    
    if chosen_type == "Locative":
        preps = open_dict(language + "WordsByType/prepositions.json")
        nouns = open_dict(language + "WordsByType/nouns.json")
        
        prep, data = rand.choice(list(preps.items()))
        translation = get_translation(data)
        
        chain = prep
        t_chain = translation
        
        noun, data = rand.choice(list(nouns.items()))
        translation = get_translation(data)
        
        chain = chain + " " + noun
        t_chain = t_chain + " " + translation
        
        return [chain, t_chain]
    elif chosen_type == "Vocative":
        names = open_dict(language + "WordsByType/names.json")
        
        name, data = rand.choice(list(names.items()))
        
        return [", " + name, ", " + name]
    elif chosen_type == "Instrumental":
        nouns = open_dict(language + "WordsByType/nouns.json")
        
        noun, data = rand.choice(list(nouns.items()))
        translation = get_translation(data)
        
        return [with_(language) + " " + noun, with_("english") + " " + translation]
    else:
        return ["", ""]

def spacing_validator(text1, text2, text3, text4):
    if text3 == "" and text4 == "":
        text = text1 + " " + text2
    elif text3 == "":
        if text4[0] == ",":
            text = text1 + " " + text2 + text4
        else:
            text = text1 + " " + text2 + " " + text4
    elif text4 == "":
        text = text1 + " " + text2 + " " + text3
    else:
        if text4[0] == ",":
            text = text1 + " " + text2 + " " + text3 + text4
        else:
            text = text1 + " " + text2 + " " + text3 + " " + text4
    
    return text

def sentence_gen(language, conj=False):
    # Choose the tense, perfectivity
    tense_options = ["past", "present", "future"]
    perfectivity_options = ["imperfect", "perfect"]
    tense = rand.choice(tense_options)
    
    if tense != "present":
        perfectivity = rand.choice(perfectivity_options)
    else:
        perfectivity = "infinitive"
        
    
    intj_weight =  0.05
    
    if rand.random() < intj_weight:
        return intj_gen(language)
    else:
        subject = subject_gen(language, tense, perfectivity)
        verb = chain_gen(language, tense, perfectivity, c_lim, verb=True)
        third = third_gen(language, tense, perfectivity)
        extras = extras_gen(language)
        
        text = spacing_validator(subject[0], verb[0], third[0], extras[0])
        translation = spacing_validator(subject[1], verb[1], third[1], extras[1])
            
        print(subject, verb, third, extras)
        return [text, translation]

#print(sentence_gen("polish", conj=False))
#print(chain_gen("polish", verb=False))
#print(chain_gen("polish", verb=True))
#print(subject_gen("polish"))

# You can check for gender, locative/vocative/instrumental, single/plural, tense/perfectivity

c_lim = 1
print(sentence_gen("polish", conj=False))

# Need a way to distinguish verbs that happen to something and verb that just happen
# Nor does it take into account perfectiveness nor tense nor singule v plural