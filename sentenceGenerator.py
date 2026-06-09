import random as rand
import json
import copy
import math
from itertools import islice

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

gender_options = ["masculine", "feminine", "neuter"]
tense_options = ["past", "present", "future"]
perfectivity_options = ["imperfect", "perfect"]
transitive_options = ["intransitive", "ambitransitive", "transitive"]

def with_(language):
    if language == "english":
        return "with"
    elif language == "polish":
        return "z"

def article_(language, word):
    if word == "":
        return word
    
    if language == "english":
        if word[0] in ["a", "e", "i", "o", "u"]:
            if rand.random() < 0.5:
                return "an " + word
            else:
                return "the " + word
        elif word[0].isupper():
            return word
        else:
            if rand.random() < 0.5:
                return "a " + word
            else:
                return "the " + word
    
    elif language == "polish":
        return word

def basic_verb_tensed(verb, tense="", perfectivity=""):
    if tense == "past":
        return verb + "ed"
    else:
        return verb

def verb_tensed(verb, tense="", perfectivity=""):
    with open("englishWordsByType/verbs.json", "r") as f:
        dictionary = json.load(f)
    
    tenses = ["past", "present", "future"]
    perfectivities = ["participle", ""]
    
    if tense in tenses:
        acceptable_tenses = [tense]
    else:
        acceptable_tenses = copy.deepcopy(tenses)
    
    if verb not in dictionary:
        return basic_verb_tensed(verb)
    
    for form in dictionary[verb]["forms"]:
        if len(acceptable_tenses) == 3:
            return form["form"]
        
        elif tense in form["tags"]:
            return form["form"]
    
    return basic_verb_tensed(verb)

def verb_handling(verb, factors):
    if factors["tense"] == "past":
        if factors["perfectivity"] == "imperfect":
            if factors["plural"]:
                return "were " + verb_tensed(verb, perfectivity="participle")
            else:
                return "was " + verb_tensed(verb, perfectivity="participle")
        else:
            return "had " + verb_tensed(verb, tense="past", perfectivity="participle")
    elif factors["tense"] == "future":
        if factors["perfectivity"] == "imperfect":
            return "will " + verb
        else:
            return "will have " + verb_tensed(verb, tense="past", perfectivity="participle")
    else:
        return pluralise_("english", verb)

def pluralise_english(word):
    if word[-1] == "y":
        return word[:-1] + "ies"
    elif word[-2:-1] == "us":
        return word[:-2] + "i"
    elif word[-1] == "s" or word[-1] == "h":
        return word + "es"
    elif word[-1] == "f":
        return word[:-1] + "ves"
    else:
        return word + "s"

def pluralise_(language, word):
    if language == "english":
        if " " in word:
            return pluralise_english(word[:word.index(" ")]) + word[word.index(" "):]
        else:
            return pluralise_english(word)
        
    elif language == "polish":
        return word

def open_dict(language, word_type):
    with open(language + "WordsByType/" + word_type + ".json") as f:
        return json.load(f)
    
def open_partial_dict(language, word_type, percent):
    max_dict = open_dict(language, word_type)
    max_length = len(max_dict)
    min_length = math.floor(max_length * percent)
    
    #print(max_dict)
    #print(len(max_dict))
    #print(length)
    return dict(islice(max_dict.items(), min(max(min_length, 5), max_length)))

def get_translation(word):
    translation = word["translations"][0]["translation"]
    return translation 

def is_valid_word(form, factors, wrong_genders, wrong_tenses, wrong_perfectivity, wrong_transitivity):
    acceptable_form = True
    
    while acceptable_form:
        for gender in wrong_genders:
            if gender in form["tags"]:
                acceptable_form = False
                break
            
        for tense in wrong_tenses:
            if tense in form["tags"]:
                acceptable_form = False
                break
        
        for perf in wrong_perfectivity:
            if perf in form["tags"]:
                acceptable_form = False
        
        for trans in wrong_transitivity:
            if trans in form["tags"]:
                acceptable_form = False
        
        if factors["plural"]:
            if "single" in form["tags"]:
                acceptable_form = False
                
            elif factors["virile"]:
                if "nonvirile" in form["tags"]:
                    acceptable_form = False
            elif "virile" in form["tags"]:
                acceptable_form = False
        elif "plural" in form["tags"]:
            acceptable_form = False
                
        if acceptable_form:
            return True
    return False

def find_word(language, word_type, factors, percent):
    # Takes in factors in a dictionary and returns a random word that matches those factors in the file given
    # Acceptable factors: "gender": str, "tense": str, "perfectivity": str, "transitive": bool, "plural": bool, "virile": bool
    words = open_partial_dict(language, word_type, percent)
    acceptable_words = []
    
    wrong_genders = copy.deepcopy(gender_options)
    wrong_genders.remove(factors["gender"])
    wrong_tenses = copy.deepcopy(tense_options)
    wrong_tenses.remove(factors["tense"])
    wrong_transitivity = copy.deepcopy(transitive_options)
    wrong_transitivity.remove(factors["transitive"])
    
    wrong_perfectivity = copy.deepcopy(perfectivity_options)
    if factors["perfectivity"] != "infinitive":
        wrong_perfectivity.remove(factors["perfectivity"])
    
    for word in words.keys():
        for form in words[word]["forms"]:
            if is_valid_word(form, factors, wrong_genders, wrong_tenses, wrong_perfectivity, wrong_transitivity):
                #print(words[word]["translations"])
                if words[word]["translations"] != []:
                    acceptable_words.append([word, words[word]["translations"][0]["translation"], form])
    
    # Choose random acceptable word
    if acceptable_words != []:
        return acceptable_words[rand.randint(0, len(acceptable_words) - 1)]
    else:
        return ["ERROR", "ERROR"]
    
def intj_gen(language, percent):
    # Return a random intj and it's most common translation
    intjs = open_partial_dict(language, "interjections", percent)
    
    intj, data = rand.choice(list(intjs.items()))
    translation = get_translation(data)
    
    return [intj, translation]

def chain_gen(language, factors, chain_limit, percent, verb=True):
    if verb:
        chainer = open_partial_dict(language, "adverbs", percent)
        finisher = find_word(language, "verbs", factors, percent)
        
        finish = finisher[2]["form"]
        #ftranslation = pluralise_("english", finisher[1])
        print(finisher[1])
        ftranslation = finisher[1]
    else:
        chainer = open_partial_dict(language, "adjectives", percent)
        finisher = open_partial_dict(language, "nouns", percent)
        
        finish, finish_data = rand.choice(list(finisher.items()))
        ftranslation = get_translation(finish_data)
        print(finish, ftranslation)
    
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
    
    if chain_len > 0:
        chain = chain + " " + finish
        t_chain = t_chain + " " + ftranslation
    else:
        chain = finish
        t_chain = ftranslation
    
    if verb:
        return [chain, t_chain]
    else:
        return [chain, t_chain, "nouns"]

def subject_gen(language, factors, percent):
    options = ["names", "pronouns", "nouns"]
    chosen_type = options[rand.randint(0, len(options)-1)]
    
    if chosen_type == "names":
        chosen_dict = open_partial_dict(language, "names", percent)
        name, data = rand.choice(list(chosen_dict.items()))
        return [name, name, "names"]
    elif chosen_type == "pronouns":
        chosen_dict = open_partial_dict(language, "pronouns", percent)
        pron, data = rand.choice(list(chosen_dict.items()))
        translation = get_translation(data)
        return [pron, translation, "pronouns"]
    else:
        return chain_gen(language, factors, c_lim, percent, verb=False)

def third_gen(language, factors, percent):
    return chain_gen(language, factors, c_lim, percent, verb=False)
    
def extras_gen(language, percent):
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
        preps = open_partial_dict(language, "prepositions", percent)
        nouns = open_partial_dict(language, "nouns", percent)
        
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
        names = open_partial_dict(language, "names", percent)
        
        name, data = rand.choice(list(names.items()))
        
        return [", " + name, ", " + name]
    elif chosen_type == "Instrumental":
        nouns = open_partial_dict(language, "nouns", percent)
        
        noun, data = rand.choice(list(nouns.items()))
        translation = get_translation(data)
        
        return [with_(language) + " " + article_(language, noun), with_("english") + " " + article_("english", translation)]
    else:
        return ["", ""]

def sentence_validator(text1, text2, text3, text4):
    text1 = text1.capitalize()
    
    text = text1 + " " + text2
    
    if text3 == "":
        if text4 == "" or (text4 != "" and text4[0] == ","):
            text = text + text4
        else:
            text = text + " " + text4
    elif text4 == "":
        text = text + " " + text3
    else:
        if text4[0] == ",":
            text = text + " " + text3 + text4
        else:
            text = text + " " + text3 + " " + text4
    
    text = text + "."
    
    return text

def choose_factors(language):
    gender = rand.choice(gender_options)
    tense = rand.choice(tense_options)
    transitive = rand.choice(transitive_options)
    plural = bool(rand.getrandbits(1))
    
    if tense != "present":
        perfectivity = rand.choice(perfectivity_options)
    else:
        perfectivity = "infinitive"
     
    if gender == "masculine" and plural:
        virile = bool(rand.getrandbits(1))
    else:
        virile = False
    
    factors = {
        "gender": gender,
        "tense": tense,
        "perfectivity": perfectivity,
        "transitive": transitive,
        "plural": plural,
        "virile": virile
    }
    
    return factors

def sentence_gen(language, percent, conj=False):
    # Choose the tense, perfectivity, transitivity, plurality
    factors = choose_factors(language)
    #factors = preset 
    
    if rand.random() < intj_weight:
        return intj_gen(language, percent)
    else:
        subject = subject_gen(language, factors, percent)
        
        verb = chain_gen(language, factors, c_lim, percent, verb=True)
        
        print(verb[1])
        verb[1] = verb_handling(verb[1], factors)
        print(verb[1])
        
        if factors["transitive"] == "transitive":
            third = third_gen(language, factors, percent)
        else:
            third = ["", ""]
            
        extras = extras_gen(language, percent)
        
        # Articles go before third and between "with_" and extras
        # Words in english need pluralising
        
        if third != ["", ""]:
            if factors["plural"]:
                third[1] = pluralise_("english", third[1])
            else:
                third[1] = article_("english", third[1])
        
        if not subject[1][0].isupper():
            if subject[2] == "nouns":
                subject[1] = article_("english", subject[1])
        
        print(factors)
        text = sentence_validator(subject[0], verb[0], third[0], extras[0])
        translation = sentence_validator(subject[1], verb[1], third[1], extras[1])
            
        print(subject, verb, third, extras)
        return [text, translation]

preset = {
    "gender": "feminine",
    "tense": "present",
    "perfectivity": "perfect",
    "transitive": False,
    "plural": False,
    "virile": False
}

commonality_limit = 1
c_lim = 1
intj_weight =  0.05
print(sentence_gen("polish", commonality_limit, conj=False))

# Current problems to solve:
# It should output all possible translations
# You should only have to open_partial_dict once per word type each run
# The root word is a form too

# Formality filters: colloquial, vulgar, impersonal, humorous, informal, formal, euphemistic, derogatory, ironic, poetic, offensive, slang, Internet, sarcastic, childish, endearing
