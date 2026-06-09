import json
from itertools import islice

with open("polishWordsByType/verbs.json") as f:
    words = json.load(f)
    
translation_tags = []
    
for word in words:
    for translation in words[word]["translations"]:
        for tag in translation["tags"]:
            if tag not in translation_tags:
                translation_tags.append(tag)
                
print(translation_tags)

x = {"hello": 1, "goodbye": 2}
y = dict(islice(x.items(), len(x)-1))
print(y)

a = "andand"
print(a[-3:])


# Forms
"""
Remove any words who's translations have the tag "form-of"
You can filter by formality based on: colloquial, vulgar, impersonal, humorous, informal, formal, euphemistic, derogatory, ironic, poetic, offensive, slang, Internet, sarcastic, childish, endearing
Remove any forms that have the tag "dialectal", "rare", "obsolete", "No tags found", "defective", "archaic", "Łowicz", "Lithuania", "dated", "uncommon", "Poznań", "regional", "Lviv"
"""

# Translations